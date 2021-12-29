# OOP_EX3
# Directed Weighted Graph Implementation - Python

This project represents a Directed Weighted Graph in python .

This project implements two main intefaces :<br />
 1) GraphInterface <br />
 2) GraphAlgoInterface <br />
 
There are two main classes that implement the intefaces :<br />
1) DiGraph : This class implements GraphInterface and has multiple functions :<br />
 - v_size : return number of nodes in the graph<br />
 - e_size : returns number of edges in the graph <br />
 - get_all_v : retruns a dictionary of all the nodes in the graph <br />
 - all_in_edges_of_node : returns a dictionary of all edges coming into node (given id)<br />
 - all_out_edges_of_node : returns a dictionary of all edges going out from node (given id)<br />
 - get_mc : returns a mode counter, the mode counter incremented with every change applied on the graph<br />
 - add_edge : given two id's of  two nodes and wiegth make a new edge connecting between them<br />
 - add_node : add a node to the graph<br />
 - get_node : given an id return the node specified with id<br />
 - remove_node : given an id , remove the node specified with this id from the graph<br />
 - remove_edge : given two id's of two nodes , removes the edge between them <br />  
2) GraphAlgo : This class implements GraphAlgoInterface and has multiple functions :<br />
 - get_graph : returns the graph wich the algorithms are applied on<br />
 - load_from_json : loads a graph from a given json file <br />
 - save_to_json : saves a graph to a json file <br />
 - shortest_path : returns a list wich contains the shortest path between two given nodes (id's) , using Dijkstra's Algorithm , and also returns the path distance<br />
 - TSP : given a list of nodes , the function returns the shortest path that visits all the nodes in the given list<br />
 - centerPoint : returns the node that has the shortest distance from all other nodes <br /> 
 - plot_graph : represents the graph<br />
 
To implement there classes we added a clas "Node" , wich represents a node in the graph and each node has a dictionary for the coming/outgoing edges <br />

## Screen shots :<br />
### check0() :<br />
![ScreenShot1](https://user-images.githubusercontent.com/94143804/147658322-538d0f9d-38be-4f25-9e17-fae0a443b67f.jpeg)<br />
### check1() :<br />
![ScreenShot2](https://user-images.githubusercontent.com/94143804/147658332-1e9a76c0-4a3f-40e1-89f3-89eb30a3a629.jpeg)<br />
### check2() :<br />
![ScreenShot3](https://user-images.githubusercontent.com/94143804/147658336-d7fa559f-4e1e-4614-8306-82aed47f54d2.jpeg)<br />

## UML diagram :<br />
![UML_diagram](https://user-images.githubusercontent.com/94143804/147659608-714a2b6b-4fd4-4e5e-82d4-83c228282028.jpeg)


