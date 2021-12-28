import math
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from math import inf

import json



def Init_Graph() -> DiGraph:

    Graph = DiGraph()

    for x in range(15):
        Graph.add_node(x)
    return Graph


def Test_center() ->DiGraph:
        graph_center = DiGraph()
        pos = [0, 0, 0]
        for n in range(4):
            graph_center.add_node(n, pos)

        graph_center.add_edge(3, 0, 2.01)
        graph_center.add_edge(3, 2, 2.05)
        graph_center.add_edge(2, 1, 11)
        graph_center.add_edge(1, 0, 12)
        graph_center.add_edge(0, 1, 2.5)
        graph_center.add_edge(1, 2, 2.1)
        graph_center.add_edge(3, 1, 2.03)
        graph_center.add_edge(2, 0, 2.9)

        return graph_center

def edges_test_Graph() -> DiGraph:
    Graph= DiGraph()

    for n in range(6):
        Graph.add_node(n)

    Graph.add_edge(2, 1, 2)
    Graph.add_edge(3, 2, 1.5)
    Graph.add_edge(0, 3, 1.2)
    Graph.add_edge(1, 2, 3)
    Graph.add_edge(3, 0, 1)
    Graph.add_edge(2, 3, 1.7)
    Graph.remove_edge(2, 1.4)

    Graph.add_edge(0, 1, 10)

    return Graph


class TestGraphAlgo(TestCase):
    graphalgo=DiGraph()


    def test_load_json_file(self):

        Algo_Grapg = GraphAlgo()

        file = '../data/A4.json'

        Algo_Grapg.load_from_json(file)

        self.assertEqual(Algo_Grapg.get_graph().v_size(), 40)

        self.assertEqual(Algo_Grapg.get_graph().e_size(), 102)


    def test_center_point(self):
        test_Graph = GraphAlgo()
        test_Graph.__init__(Test_center())


        self.assertEqual(str(3), str(test_Graph.centerPoint()[0]))
        self.assertNotEqual(0, test_Graph.centerPoint())
        self.assertNotEqual(1, test_Graph.centerPoint())
        self.assertNotEqual(2, test_Graph.centerPoint())



    def test_save_json_file(self):

        graph = GraphAlgo(edges_test_Graph)

        graph.save_to_json("graph111.json")
        f = open("graph111.json")
        d = json.load(f)

        weight = d['Edges'][2]['w']

        self.assertEqual(weight, 1.3)




    def test_shortestpath(self):
        test_Graph = GraphAlgo()

        test_Graph.__init__(Init_Graph())

        self.assertEqual(len(test_Graph.get_graph().get_all_v()), 15)

        test_Graph.get_graph().add_edge(0, 1, 1)
        test_Graph.get_graph().add_edge(0, 2, 3)
        test_Graph.get_graph().add_edge(1, 4, 1)
        test_Graph.get_graph().add_edge(2, 6, 1)
        test_Graph.get_graph().add_edge(2, 1, 3)
        self.assertEqual(test_Graph.shortest_path(0, 0), (0, [0]))
        self.assertEqual(test_Graph.shortest_path(0, 6), (4, [0, 2, 6]))
        self.assertEqual(test_Graph.shortest_path(0, 4), (2, [0, 1, 4]))
        self.assertEqual(test_Graph.shortest_path(0, 9), (inf, []))

    def test_tsp(self):
        g = DiGraph()

        for n in range(8):
            g.add_node(n)
        g.add_edge(0, 1, 4)
        g.add_edge(0, 4, 8)
        g.add_edge(1, 0, 4.1)
        g.add_edge(1, 2, 4.3)
        g.add_edge(1, 3, 4.9)
        g.add_edge(2, 3, 4.1)
        g.add_edge(3, 4, 5.1)
        g.add_edge(4, 2, 3.5)
        g_algo = GraphAlgo(g)

        print(g_algo.TSP([1, 2, 4]))