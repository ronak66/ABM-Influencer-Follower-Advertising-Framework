import random
import numpy as np
from queue import Queue
import matplotlib.pyplot as plt

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from InfluencerAgent import InfluencerAgent

from RandomGenerator import randomTrueFalse


class InfluencerAdvertisingModel(Model):

    def __init__(self, width, height, Graph, node_ids, product_cost, hiring_budget, grid=1):
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
        self.current_step = 1
        self.visited_nodes = set()
        self.engage_count = 0
        self.total_hiring_cost = 0
        self.hiring_budget = hiring_budget
        self.setup_datacollector()
        self.generate_agents()
        self.assign_attributes()

        if(grid==1):
            self.grid = MultiGrid(width, height, True)
            self.setup_grid()

        # self.initialize_campaign_marketers(node_ids)
        self.campaign_marketers = node_ids

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

    def assign_attributes(self):
        for node_id, agent in self.id_agent_mp.items():
            if(node_id in self.graph.graph.keys()):
                degree = len(self.graph.graph[node_id])
                agent.set_outDegree(degree)
                agent.set_engagement_rate()
                agent.set_hiring_cost()
                # agent.set_sigStrength(agent.out_degree / 3383)
                agent.set_sigStrength(1)
            else:
                agent.set_outDegree(0)

    def update_influence_wrt_engagement(self):
        gamma = 0.7
        for agent_id, edges in self.graph.graph.items():
            engagement_rate = self.id_agent_mp[agent_id].engagement_rate
            for edge in edges:
                if(randomTrueFalse(engagement_rate/100)):
                    edge.set_weight(edge.weight + gamma)


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

    def initialize_campaign_marketers_at_step(self):
        '''
        All the node ids who start the campaign propagation
        '''
        for node_id in self.campaign_marketers.get(self.current_step,[]):
            print("="*80,self.id_agent_mp[node_id].get_outDegree(),sep='\n')
            self.id_agent_mp[node_id].hired = True
            self.total_hiring_cost += self.id_agent_mp[node_id].hiring_cost
            self.bfs_queue.put(node_id)

    def sig_decay(self, sig_strength, bfs_level):
        return sig_strength * (bfs_level**-(2))

    def propagate_from_node(self,node_id):
        '''
        Given a node, propagates the campaign
        Makes the decision for all the neighours of the given node
        '''
        if(node_id in self.campaign_marketers.get(self.current_step,[])):
            influenced_by = node_id
        else:
            influenced_by = self.id_agent_mp[node_id].influenced_by_node_id

        signal_strength = self.id_agent_mp[influenced_by].sig_strength
        engagement_rate = self.id_agent_mp[node_id].engagement_rate
        hired = self.id_agent_mp[node_id].hired

        gamma = 0.7

        if(node_id in self.graph.graph.keys()):
            for _, ngb_edge in enumerate(self.graph.graph[node_id]):

                ngb_id = ngb_edge.node_id
                weight = ngb_edge.weight
                ngb_agent = self.id_agent_mp[ngb_id]
                if(hired and randomTrueFalse(engagement_rate/100)):

                    weight += gamma
                    self.engage_count += 1

                if(ngb_agent.decision == False and ngb_agent.hired == False):
                    self.visited_nodes.add(ngb_agent)
                    decay_factor = self.sig_decay(signal_strength, self.current_step)
                    decision = ngb_agent.make_decision(weight, decay_factor, self.product_cost)
                    self.update_ngb_nodes_interest(node_id, decision)
                    if(decision == True):
                        ngb_agent.influenced_by_node_id = influenced_by
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

    def interest_count(self):
        count = [0,0,0,0,0,0,0,0,0,0]
        for _, agent in self.id_agent_mp.items():
            if(agent.interest<=0.1 and agent.interest>=0): count[0] += 1
            if(agent.interest<=0.2 and agent.interest>0.1): count[1] += 1
            if(agent.interest<=0.3 and agent.interest>0.2): count[2] += 1
            if(agent.interest<=0.4 and agent.interest>0.3): count[3] += 1
            if(agent.interest<=0.5 and agent.interest>0.4): count[4] += 1
            if(agent.interest<=0.6 and agent.interest>0.5): count[5] += 1
            if(agent.interest<=0.7 and agent.interest>0.6): count[6] += 1
            if(agent.interest<=0.8 and agent.interest>0.7): count[7] += 1
            if(agent.interest<=0.9 and agent.interest>0.8): count[8] += 1
            if(agent.interest<=1 and agent.interest>0.9): count[9] += 1

        return count

    def interest_histogram(self, interest_data):
        bin_edges = np.arange(0.1, 1.1, 0.1)
        plt.figure(self.current_step)
        plt.bar(bin_edges, interest_data, width = 0.05, alpha = 0.9)
        plt.grid(axis = 'y')
        plt.xticks(bin_edges)
        plt.xlabel('Interval (upperlimit)', horizontalalignment='center')
        plt.ylabel('Number of Agents')
        plt.title('Distribution of Interest in the Agent Population')
        plt.savefig('../experimental_results/interest_distribution/gamma=0.01/step{}.png'.format(self.current_step))

    def step(self):
        print('interest Distribution: ', self.interest_count())

        self.initialize_campaign_marketers_at_step()
        print('Total Hiring Cost: ', self.total_hiring_cost, 'Hiring Budget: ', self.hiring_budget)
        n = self.bfs_queue.qsize()
        self.datacollector.collect(self)
        for _ in range(n):
            node_id = self.bfs_queue.get()
            self.propagate_from_node(node_id)
        print('Total people reached: ', len(self.visited_nodes))            
        self.current_step += 1
