import random
import networkx as nx


class Graph():

    def __init__(self,n,k,p=0.5):
        self.G = nx.watts_strogatz_graph(n = n, k = k, p = 0.5)
        self.graph = {}

        self.create_weighted_directed_graph()

    def create_weighted_directed_graph(self):
        for from_node,to_node in self.G.edges():
            edge = Edge(to_node,random.random())
            if(from_node in self.graph.keys()):
                self.graph[from_node].append(edge)
            else:
                self.graph[from_node] = [edge]

    def nodes(self):
        return self.G.nodes()
class Edge():

    def __init__(self,node_id,weight):
        self.node_id = node_id
        self.weight = weight