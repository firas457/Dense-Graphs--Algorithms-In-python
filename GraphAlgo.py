import sys
from GraphAlgoInterface import GraphAlgoInterface
from Node import Node
from GraphInterface import GraphInterface
from DiGraph import DiGraph
import json
from typing import List
from itertools import permutations
from numpy import inf
import random
import queue as Queue
import queue as Q
import matplotlib.pyplot as plot



class GraphAlgo(GraphAlgoInterface):


    def __init__(self, G: DiGraph = None):
        self.G = G




    def get_graph(self) -> GraphInterface:
        return self.G





    def load_from_json(self, file_name: str) -> bool:

        try:

            with open(file_name) as file:

                dictionary_json = json.load(file)

            new_graph = DiGraph()

            for n in dictionary_json["Nodes"]:

                node_key = n["id"]
                pos_tuple = None

                if "pos" in n:
                    pos = n["pos"]
                    pos_tuple = tuple(map(float, pos.split(",")))
                new_graph.add_node(node_key, pos_tuple)

            for e in dictionary_json["Edges"]:
                src = int(e["src"])
                dest = int(e["dest"])
                weight = float(e["w"])

                new_graph.add_edge(src, dest, weight)

            self.G = new_graph
            return True

        except Exception as exception:
            print(exception)
            return False




    def save_to_json(self, file_name: str) -> bool:

        graph_to_json = {}

        nodes = []

        edges =[]

        for n in self.G.get_all_v().values():

            nodes.append({"id": n.get_id()})

            for dest, weight in n.edges_from_node().items():

                edges.append({"src": n.get_id(), "dest": dest, "w": weight})

        graph_to_json["Nodes"] = nodes

        graph_to_json["Edges"] = edges


        try:

            with open(file_name, 'w') as f:

                json.dump(graph_to_json, f)
            return True


        except Exception as exception:
            print(exception)
            return False



    def shortest_path(self, id1: int, id2: int) -> (float, list):
        for n in self.G.get_all_v().values():
            n.reset()

        queue = Queue.PriorityQueue()

        if id1 == id2:

            return 0, [id1]

        src = self.G.get_node(id1)

        dest= self.G.get_node(id2)


        if src is None or dest is None:

            return float('inf'), []


        for dest_e, weight_e in src.edges_from_node().items():

            queue.put((weight_e, src.get_id(), dest_e))

        src.set_weight(0)


        src.set_info('BLACK')

        while not  queue.empty():

            edge =  queue.get()

            weight = edge[0]

            source_node= edge[1]
            dest_node= edge[2]

            connected_node = self.G.get_node(dest_node)


            if weight < connected_node.get_weight():

                connected_node.set_weight(weight)

                connected_node.set_Tag(source_node)

            if connected_node.get_info() != 'BLACK':

                for dest_edge, weight in connected_node.edges_from_node().items():

                    queue.put((weight + connected_node.get_weight(), connected_node.get_id(), dest_edge))
                connected_node.set_info('BLACK')

        node_next = dest

        if node_next.get_Tag() == -1:

            return float('inf'), []

        path = list()

        while node_next.get_Tag() != -1:

            path.append(node_next.get_id())
            node_next = self.G.get_node(node_next.get_Tag())

        path.append(node_next.get_id())
        path.reverse()



        return self.G.get_node(path[-1]).get_weight(), path



    def hfunc(self, src, list_node):
        pathtaken = []
        list = []
        temp = []

        for tempnode in list_node:
            if tempnode != src:
                temp.append(tempnode)
        min = sys.maxsize
        pe = permutations(temp)


        for currp in pe:
            list.clear()
            related = True
            curr = 0
            tempn = src
            list.append(tempn)


            for node2 in currp:

                weight = self.shortest_path(tempn, node2)[0]


                for n in range(len(self.shortest_path(tempn, node2)[1])):
                    if n != 0:
                        list.append(self.shortest_path(tempn, node2)[1][n])


                if weight == float('inf'):
                    related = False
                    break

                curr += weight
                tempn = node2


            if related:
                if min > curr:
                    min = curr
                    pathtaken = list


        return pathtaken, min




    def TSP(self, node_lst: List[int]) -> (List[int], float):
        max_w = sys.maxsize

        for src in node_lst:

            if self.hfunc(src, node_lst)[1] < max_w :

                max_w = self.hfunc(src, node_lst)[1]

                pathtaken, weight = self.hfunc(src, node_lst)


        if max_w  == sys.maxsize:

            return [], float('inf')


        return pathtaken,weight







    def centerPoint(self) -> (int, float):

        if self.G.nodes_size == 0:
            return None, None

        min = inf
        id = 0
        max = 0


        for n1 in self.G.nodes.values():
            for n2 in self.G.nodes.values():
                d = self.shortest_path(n1.get_id(), n2.get_id())[0]
                if d > max:
                    max = d
            if max < min:
                min = max
                id = n1.get_id()
            max = 0

        ans = (id, min)

        return ans




    def plot_graph(self) -> None:

        arrow_width = 0.00002
        arrow_head_width = 10 * arrow_width
        arrow_head_length = 13 * arrow_width

        fig, ax = plot.subplots()

        minx=float("inf")
        miny=float("inf")
        maxx=0
        maxy =0

        for n in self.G.get_all_v().values():

            minx = n.get_position()[0] if n.get_position()[0] < minx else minx
            miny = n.get_position()[1] if n.get_position()[1] < miny else miny
            maxx = n.get_position()[0] if n.get_position()[0] > maxx else maxx
            maxy = n.get_position()[1] if n.get_position()[1] > maxy else maxy

            tuple = (n.get_position()[0], n.get_position()[1])

            draw_node = plot.Circle(tuple, 0.00015, color='red')
            ax.add_artist(draw_node)

            pos0=n.get_position()[0] - 0.000135
            pos1=n.get_position()[1] + 0.00025

            plot.text(pos0, pos1, str(n.get_id()), fontsize=10, color="red")

            source_pos = n.get_position()

            for destintion_node in n.edges_from_node():

                dest_node_pos = self.G.get_node(destintion_node).get_position()

                plot.arrow(source_pos[0], source_pos[1], dest_node_pos[0] - source_pos[0],
                           dest_node_pos[1] - source_pos[1], width=arrow_width, head_width=arrow_head_width,
                           head_length=arrow_head_length, length_includes_head=True)


        offset = 0.0005
        plot.ylim(miny - offset, maxy + offset)
        plot.xlim(minx - offset, maxx + offset)


        plot.xlabel('x - axis')

        plot.ylabel('y - axis')


        plot.title('Graph')


        plot.show()
