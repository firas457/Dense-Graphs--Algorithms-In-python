from unittest import TestCase

from src.DiGraph import DiGraph



def Init_Graph() -> DiGraph:
    test_graph = DiGraph()
    for x in range(15):
        test_graph.add_node(x)
    return test_graph







class Test_Graph(TestCase):




    def test_edge_size(self):
        graph = Init_Graph()
        self.assertEqual(graph.e_size(), 0)
        graph.add_edge(0, 4, 1)
        graph.add_edge(0, 2, 4)
        graph.add_edge(3, 4, 1)
        graph.add_edge(0, 3, 1)
        graph.add_edge(2,3,1)
        graph.add_edge(3,2,1)
        graph.add_edge(2,4,1)
        self.assertEqual(graph.e_size(), 7)

    def test_remove_node(self):
        graph = Init_Graph()
        self.assertEqual(graph.get_node(4).get_id(), 4)
        graph.remove_node(4)
        self.assertIsNone(graph.get_node(4))

    def test_remove_edge(self):
        graph = Init_Graph()
        self.assertFalse(graph.remove_edge(0, 1))
        graph.add_edge(0, 1, 1.5)
        self.assertTrue(graph.remove_edge(0, 1))

    def test_v_size(self):
        graph = Init_Graph()
        self.assertEqual(graph.v_size(), 15)


    def test_get_mc(self):

        test_graph = Init_Graph()

        self.assertEqual(test_graph.get_mc(), 15)
        test_graph.add_edge(1, 3, 2)
        test_graph.add_edge(0, 2, 1)
        test_graph.add_edge(2, 4, 3)
        test_graph.add_edge(2, 3, 1.5)
        test_graph.add_edge(4, 1, 2 )
        self.assertEqual(test_graph.get_mc(), 20)


    def test_add_node(self):
        test_graph = Init_Graph()
        self.assertEqual(test_graph.get_node(15), None)
        test_graph.add_node(15)
        self.assertEqual(test_graph.get_node(15).get_id(), 15)


    def test_get_node(self):
        test_graph = Init_Graph()
        self.assertEqual(test_graph.get_node(15), None)
        test_graph.add_node(15)
        self.assertEqual(test_graph.get_node(15).get_id(), 15)


