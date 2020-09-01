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
        self.interest = RandomGenerator(0, 1)
        self.budget = RandomGenerator(0, 100)
        self.active = True
        self.sig_strength = 0
        self.influenced_by_node_id = -1

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

    def update_interest(self, influence, decision):
        self.interest_update_function(influence, decision)

    def make_decision(self, influence, signal_strength, product_cost):
        self.decision = self.decision_function(influence, signal_strength, product_cost)
        return self.decision

    def interest_update_function(self, influence, decision):
        gamma = 0.01
        if decision:
            self.interest = self.interest + (self.interest*influence)
        else:
            if randomTrueFalse(gamma):
                self.interest = self.interest - (self.interest*influence)

        if(self.interest<0): self.interest = 0
        if(self.interest>1): self.interest = 1

    def decision_function(self, influence, signal_strength, product_cost):
        self.active = randomTrueFalse(0.9)
        if self.budget >= product_cost and self.active:
            decision = RandomGenerator(0, 1) < (self.interest * influence * signal_strength)
        else:
            decision = False
        return decision
