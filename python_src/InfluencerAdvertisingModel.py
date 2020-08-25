import random
from queue import Queue

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from InfluencerAgent import InfluencerAgent
class InfluencerAdvertisingModel(Model):

    def __init__(self, width, height, Graph, node_ids, product_cost, grid=1):
        '''
        Graph = {
            <node id> : [ <Edge Object> ]
        }
        '''
        self.num_agents = len((Graph.get_nodes()))
        self.graph = Graph
        self.bfs_queue = Queue()
        self.running = True
        self.product_cost = product_cost

        self.setup_datacollector()
        self.generate_agents()
        self.assign_outdegree()

        if(grid==1):
            self.grid = MultiGrid(width, height, True)
            self.setup_grid()

        self.initialize_campaign_marketers(node_ids)

    def number_bought(self,model):
        count=0
        for _, agent in model.id_agent_mp.items():
            if(agent.decision == True): count+=1
        return count

    def no_bought_every_timestep(self,model):
        return model.bfs_queue.qsize()

    def setup_datacollector(self):
        self.datacollector = DataCollector(
            model_reporters={
                "No bought at every timestep": self.no_bought_every_timestep,
                "No who bought": self.number_bought
            }
            # agent_reporters={"Wealth": "wealth"}
        )

    def generate_agents(self):
        '''
        Creates mapping with keys as the node id, and value as agent class
        '''
        self.id_agent_mp = {}
        for node_id in self.graph.get_nodes():
            agent = InfluencerAgent(node_id,self)
            self.id_agent_mp[node_id] = agent

    def assign_outdegree(self):
        for node_id, agent in self.id_agent_mp.items():
            if(node_id in self.graph.graph.keys()):
                agent.set_outDegree(len(self.graph.graph[node_id]))
            else:
                agent.set_outDegree(0)

    def setup_grid(self,random_position=1):
        '''
        Places agents on the grid
        '''
        if(random_position==1):
            for node_id in self.graph.get_nodes():
                x, y = random.choice(list(self.grid.empties))
                self.grid.place_agent(self.id_agent_mp[node_id], (x, y))
        else:
            node_id = 0
            for row in range(self.grid.width):
                for col in range(self.grid.height):
                    if(node_id == self.num_agents):
                        return
                    self.grid.place_agent(self.id_agent_mp[node_id], (col, row))
                    node_id+=1

    def initialize_campaign_marketers(self,node_ids):
        '''
        All the node ids who start the campaign propagation
        '''
        for node_id in node_ids:
            print("="*80,self.id_agent_mp[node_id].get_outDegree(),sep='\n')
            self.id_agent_mp[node_id].hired = True
            self.bfs_queue.put(node_id)

    def propagate_from_node(self,node_id):
        '''
        Given a node, propagates the campaign
        Makes the decision for all the neighours of the given node
        '''

        if(node_id in self.graph.graph.keys()):
            for _, ngb_edge in enumerate(self.graph.graph[node_id]):

                ngb_id = ngb_edge.node_id
                weight = ngb_edge.weight
                ngb_agent = self.id_agent_mp[ngb_id]


                if(ngb_agent.decision == False and ngb_agent.hired == False):
                    decision = ngb_agent.make_decision(weight, self.product_cost)
                    self.update_ngb_nodes_interest(node_id, decision)
                    if(decision == True):
                        self.bfs_queue.put(ngb_id)

    def update_ngb_nodes_interest(self,node_id, decision):
        '''
        Given the node (who acknowledge the campaign), update interest of it's neighbours
        '''
        if(node_id in self.graph.graph.keys()):
            for _, ngb_edge in enumerate(self.graph.graph[node_id]):

                ngb_id = ngb_edge.node_id
                weight = ngb_edge.weight
                ngb_agent = self.id_agent_mp[ngb_id]

                if(ngb_agent.decision == False):
                    ngb_agent.update_interest(weight, decision)

    def step(self):
        n = self.bfs_queue.qsize()
        self.datacollector.collect(self)
        for _ in range(n):
            node_id = self.bfs_queue.get()
            self.propagate_from_node(node_id)
        # node_id = self.bfs_queue.get()
        # self.propagate_from_node(node_id)
