from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid, NetworkGrid
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import NetworkModule
from mesa.datacollection import DataCollector
from mesa.visualization.ModularVisualization import ModularServer
import random
import networkx as nx

class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model,start):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.start = start

    def give_money(self):
        self.wealth-=1

    def step(self):
        if self.wealth > 0:
            self.give_money()

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.running = True
        self.agents = []
        graph = nx.fast_gnp_random_graph(100, 0.1)
        # self.G = NetworkGrid(graph)
        # print((graph.nodes))
        # print('='*80)
        # print(self.G.get_all_cell_contents())
        # Create agents
        k = 0
        j = 0
        
        for i in range(self.num_agents):
            if(i==0 and j==0): start = 1
            else: start = 0

            a = MoneyAgent(i, self, start)

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (k, j))
            if(j==9):
                j=0
                k+=1
            else:
                j+=1

            # self.G.place_agent(a,i)

            self.agents.append(a)

    def step(self):
        x = random.choice(range(len(self.agents)))
        if(self.agents[x].start != 1):
            self.agents[x].step()


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}
    if agent.wealth > 0:
        if(agent.start == 1):
            portrayal["Color"] = "blue"
            portrayal["Layer"] = 0
        else:
            portrayal["Color"] = "red"
            portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal

if __name__ == '__main__':
    # model = MoneyModel(10)
    # for i in range(10):
    #     model.step()
    grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
    # grid = NetworkModule(agent_portrayal)
    server = ModularServer(MoneyModel,
                    [grid],
                    "Money Model",
                    {"N":9, "width":10, "height":10})
    server.port = 8521 # The default
    server.launch()