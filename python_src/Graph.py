import random
import networkx as nx


class Graph():

    def __init__(self,graph_type,filepath='',n=100,k=10,p=0.5):        
        self.graph = {}
        if(graph_type=='networkx'):
            self.create_networkx_graph(n,k,p)
        if(graph_type=='twitter'):
            self.create_twitter_graph(filepath)

        self.assign_edge_weights()
        
    def assign_edge_weights(self):
        for from_node,to_node in self.edges:
            edge = Edge(to_node,random.random())
            if(from_node in self.graph.keys()):
                self.graph[from_node].append(edge)
            else:
                self.graph[from_node] = [edge]

    def create_networkx_graph(self,n,k,p):
        G = nx.watts_strogatz_graph(n=n, k=k, p=p)
        self.edges = list(G.edges())
        self.nodes = list(G.nodes())
    
    def create_twitter_graph(self,filepath):
        self.edges = []
        self.nodes = set()
        with open(filepath) as file:
            for line in file:
                x, y = [int(node_id) for node_id in line.split(' ')]
                self.edges.append((y, x))
                self.nodes.add(x)
                self.nodes.add(y)
        self.nodes = list(self.nodes)

    def get_nodes(self):
        return self.nodes
class Edge():

    def __init__(self,node_id,weight):
        self.node_id = node_id
        self.weight = weight