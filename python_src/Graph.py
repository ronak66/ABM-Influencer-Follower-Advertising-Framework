import random
import networkx as nx

import fittingCode.socialModels as sm
from RandomGenerator import gaussianRandomgenerator


class Graph():

    def __init__(self):        
        self.graph = {}
        
    def assign_edge_weights(self):
        for from_node,to_node in self.edges:
            edge_weight = self.get_random_edge_weight('random')
            edge = Edge(to_node,edge_weight)
            if(from_node in self.graph.keys()):
                self.graph[from_node].append(edge)
            else:
                self.graph[from_node] = [edge]

    def get_random_edge_weight(self,rand_type):
        if(rand_type == 'random'):
            return random.random()
        if(rand_type == 'gauss'):
            return gaussianRandomgenerator(0,1,0.7,0.1)
        
    def create_networkx_graph(self,n,k,p):
        # G = nx.watts_strogatz_graph(n=n, k=k, p=p)
        G = sm.nearestNeighbor_mod(n,k,p)
        self.edges = list(G.edges())
        self.nodes = list(G.nodes())

        self.assign_edge_weights()
    
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

        self.assign_edge_weights()

    def get_nodes(self):
        return self.nodes
        
class Edge():

    def __init__(self,node_id,weight):
        self.node_id = node_id
        self.weight = weight

    def set_weight(self,weight):
        if(weight>1):
            weight = 1
        if(weight<0):
            weight = 0
        self.weight = weight