from mesa import Agent
from RandomGenerator import *

class InfluencerAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.hired = False
        self.out_degree = 0
        self.decision = False
        self.interest = RandomGenerator(0, 1)
        self.resources = RandomGenerator(0, 100)
        self.count = 0
        self.active = randomTrueFalse(0.9)

    def get_outDegree(self):
        return self.out_degree

    def set_outDegree(self, out_degree):
        self.out_degree = out_degree

    def get_interest(self):
        return self.interest

    def get_decision(self):
        return self.decision

    def update_interest(self, influence, decision):
        self.interest_update_function(influence, decision)

    def make_decision(self, influence, product_cost):
        self.decision = self.decision_function(influence, product_cost)
        return self.decision

    def interest_update_function(self, influence, decision):
        if decision:
            self.interest = self.interest + (self.interest*influence)**100000
        else:
            self.interest = self.interest - (self.interest*influence)**100000

    def decision_function(self, influence, product_cost):
        if self.resources >= product_cost:
            decision = RandomGenerator(0, 1) < self.interest*influence
        else:
            decision = False
        return decision
