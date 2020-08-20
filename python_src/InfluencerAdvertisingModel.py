import random
from queue import Queue

from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from InfluencerAgent import InfluencerAgent

class InfluencerAdvertisingModel(Model):

    def __init__(self, width, height, Graph):
        '''
        Graph = {
            <node id> : [ <Edge Object> ]
        }
        '''
        self.num_agents = (Graph.nodes())
        self.grid = MultiGrid(width, height, True)
        self.running = True
        self.graph = Graph
        self.bfs_queue = Queue()

        self.generate_agents()
        self.setup_grid()

    def initialize_campaign_marketers(self,node_ids):
        '''
        All the node ids who start the campaign propagation
        '''
        for node_id in node_ids:
            self.id_agent_mp[node_id].hired = True
            self.bfs_queue.put(node_id)

    def generate_agents(self):
        '''
        Creates mapping with keys as the node id, and value as agent class
        '''
        self.id_agent_mp = {}
        for node_id in self.graph.nodes():
            agent = InfluencerAgent(node_id,self)
            self.id_agent_mp[node_id] = agent

    def setup_grid(self):
        '''
        Places agents on the grid
        '''
        node_id = 0
        for row in range(self.grid.width):
            for col in range(self.grid.height):
                if(node_id == self.num_agents):
                    return
                self.grid.place_agent(self.id_agent_mp[node_id], (col, row))
                node_id+=1

    def setup(self):
        n = self.bfs_queue.qsize()
        for _ in range(n):
            node_id = self.bfs_queue.get()
            self.propagate_from_node(node_id)


    def propagate_from_node(self,node_id):
        if(node_id in self.graph.keys()):
            for _, ngb_edge in enumerate(self.graph[node_id]):

                ngb_id = ngb_edge.node_id
                weight = ngb_edge.weight
                ngb_agent = self.id_agent_mp[ngb_id]

                decision = ngb_agent.make_decision(weight)
                self.update_ngb_nodes_interest(node_id)

    def update_ngb_nodes_interest(self,node_id):
        pass