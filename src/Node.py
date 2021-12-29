
import random


class Node():

    def  __init__(self,id:int,pos:tuple = None):
        self._id = id
        self.edges_from = {}
        self.edges_to = {}
        self.weight: float = float("inf")
        self.tag: int = -1
        self.info: str = 'WHITE'
        rand_x = random.uniform(35.185,35.215)
        rand_y=random.uniform(32.098,32.11)
        self.position : tuple= pos if pos is not None else (rand_x,rand_y)


    def reset (self) :
        self.weight:float=float("inf")
        self.info:str = "White"
        self.id : int = -1
        self.tag: int = -1

    def edges_to_node(self):
        return self.edges_to

    def edges_from_node(self):
        return self.edges_from

    def get_id(self) -> int:
        return self._id

    def get_Tag(self) -> int:
        return self.tag

    def set_Tag(self, t: int)->None:
        self.tag = t

    def get_position(self)->tuple:
        return self.position


    def get_weight(self) -> float:
        return self.weight

    def set_weight(self, w: float)-> None:
        self.weight = w

    def get_info(self)->str:
        return self.info

    def set_info(self,info: str)->None:
        self.info=info

    def out_edges(self,dest: int, weight: float):
        self.edges_from[dest] = weight

    def in_edges(self,src:int, weight: float):
        self.edges_to[src] = weight

    def remove_out_edge(self,dest:int) ->None:
        del self.edges_from[dest]

    def remove_in_edge(self,src:int)->None:
        del self.edges_to[src]

    def edge_exists(self, id1: int) -> bool:
        if id1 in self.edges_from:
            return True
        else:
            return False



    def __repr__(self):
        in_length = len(self.edges_to)
        out_length = len(self.edges_from)
        return "" + str(self._id) + "number of edges in : " + str(in_length) + "number of edges out : " + str(out_length) + ""



