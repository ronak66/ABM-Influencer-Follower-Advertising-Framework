from mesa import Agent
from RandomGenerator import RandomGenerator, randomTrueFalse, gaussianRandomgenerator
import random
class InfluencerAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.hired = False
        self.hiring_cost = 0
        self.out_degree = 0
        self.decision = False
        self.interest = gaussianRandomgenerator(0, 1, 0.5, 0.2)
        # self.interest = RandomGenerator(0,1)
        self.budget = RandomGenerator(0, 100)
        self.active = True
        self.sig_strength = 0
        self.influenced_by_node_id = -1
        self.engagement_rate = 0

    def get_outDegree(self):
        return self.out_degree

    def set_outDegree(self, out_degree):
        self.out_degree = out_degree

    def set_sigStrength(self, sig_strength):
        self.sig_strength = sig_strength

    def get_interest(self):
        return self.interest

    def get_decision(self):
        return self.decision

    def set_engagement_rate(self):
        # Twitter =============================================
        # mapping = {
        #     (0,50): 30,
        #     (51,200): 25,
        #     (201,700): 18,
        #     (701,1500): 12,
        #     (1501,3000): 5,
        #     (3001,None): 1
        # }

        # Google Plus =========================================
        mapping = {
            (0,500):30,
            (501,1000):25,
            (1001,2100):18,
            (2101,4200):12,
            (4201,8500):5,
            (8501,18000):1
        }

        # Networkx ================================================
        # mapping = {
        #     (1,75): 30,
        #     (76,150): 25,
        #     (151,300): 18,
        #     (301,500): 12,
        #     (501,700): 5,
        #     (701,None): 1
        # }


        for interval,rate in mapping.items():
            lower, upper = interval
            if(self.out_degree>=lower):
                if(upper == None):
                    self.engagement_rate = rate
                elif(self.out_degree<=upper):
                    self.engagement_rate = rate
                    break

    def set_hiring_cost(self):
        cost_per_post_per_follower = 0.01
        self.hiring_cost = cost_per_post_per_follower*self.out_degree

    def update_interest(self, influence, decision):
        self.interest_update_function(influence, decision)

    def make_decision(self, influence, signal_strength, product_cost):
        self.decision = self.decision_function(influence, signal_strength, product_cost)
        return self.decision

    def interest_update_function(self, influence, decision):
        gamma = 0.001
        if decision:
            self.interest = self.interest + (self.interest*influence)
        else:
            if randomTrueFalse(gamma):
                self.interest = self.interest - (self.interest*influence)

        if(self.interest<0): self.interest = 0
        if(self.interest>1): self.interest = 1

    def decision_function(self, influence, signal_strength, product_cost):
        self.active = randomTrueFalse(0.95)
        if self.budget >= product_cost and self.active:
            decision = RandomGenerator(0, 1) < (self.interest * influence * signal_strength)
        else:
            decision = False
        return decision
