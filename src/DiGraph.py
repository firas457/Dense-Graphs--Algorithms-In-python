from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.nodes_size = 0
        self.edges_size = 0
        self.mode_counter = 0
        

    def v_size(self)-> int:
        return self.nodes_size

    def e_size(self)-> int:
        return self.edges_size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_to_node()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_from_node()

    def get_mc(self) -> int:
        return self.mode_counter

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes or id2 not in self.nodes or self.nodes[id1].edge_exists(id2):
            return False

        self.nodes[id1].out_edges(id2,weight)
        self.nodes[id2].in_edges(id1,weight)

        self.mode_counter +=1
        self.edges_size+=1

        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False

        self.nodes[node_id]=Node(node_id,pos)
        self.mode_counter+=1
        self.nodes_size+=1
        return True

    def get_node(self, node_id: int) -> Node:
        return self.nodes.get(node_id)

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        for key in self.nodes[node_id].edges_to_node():
            self.nodes[key].remove_in_edges(node_id)
            self.mode_counter+=1

        for key in self.nodes[node_id].edges_from_node():
            self.nodes[key].remove_out_edges(node_id)
            self.mode_counter += 1


        del self.nodes[node_id]
        self.nodes_size-=1
        self.mode_counter+=1

        return True
        
        

        

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return False
        if self.nodes[node_id1].edge_exists(node_id2) == False:
            return False

        self.nodes[node_id1].remove_out_edge(node_id2)
        self.nodes[node_id2].remove_in_edge(node_id1)
        self.edges_size-=1
        self.mode_counter+=1

        return True


    def __repr__(self):
        return "number of nodes : " + str(self.nodes_size)+" and number of edges : " + str(self.edges_size) + ""
