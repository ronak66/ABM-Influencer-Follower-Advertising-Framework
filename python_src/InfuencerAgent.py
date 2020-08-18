from mesa import Agent

class InfluencerAget(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def setup(self):
        pass