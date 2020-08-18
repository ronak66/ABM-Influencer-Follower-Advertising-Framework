from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.visualization.modules import CanvasGrid
from mesa.datacollection import DataCollector
from mesa.visualization.ModularVisualization import ModularServer
import random

class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model,start):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.start = start

    # def move(self):
    #     possible_steps = self.model.grid.get_neighborhood(
    #         self.pos,
    #         moore=True,
    #         include_center=False)
    #     new_position = self.random.choice(possible_steps)
    #     self.model.grid.move_agent(self, new_position)

    def give_money(self):
        # cellmates = self.model.grid.get_cell_list_contents([self.pos])
        # if len(cellmates) > 1:
        #     other_agent = self.random.choice(cellmates)
        #     other_agent.wealth += 1
        #     self.wealth -= 1
        self.wealth-=1

    def step(self):
        # self.move()
        if self.wealth > 0:
            self.give_money()


def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum( xi * (N-i) for i,xi in enumerate(x) ) / (N*sum(x))
    return (1 + (1/N) - 2*B)

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        # self.schedule = RandomActivation(self)
        self.running = True
        self.agents = []

        # Create agents
        k = 0
        j = 0
        
        for i in range(self.num_agents):
            if(i==0 and j==0): start = 1
            else: start = 0

            a = MoneyAgent(i, self, start)
            # self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            # print(i,j)
            self.grid.place_agent(a, (k, j))
            if(j==9):
                j=0
                k+=1
            else:
                j+=1
            # if(j==self.grid.height-1):
            #     i+=1
            #     j=0
            # else:
            #     j+=1
            self.agents.append(a)

        # self.datacollector = DataCollector(
        #     model_reporters={"Gini": compute_gini},
        #     agent_reporters={"Wealth": "wealth"})

    def step(self):
        # self.datacollector.collect(self)
        # self.schedule.step()
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
    server = ModularServer(MoneyModel,
                    [grid],
                    "Money Model",
                    {"N":100, "width":10, "height":10})
    server.port = 8521 # The default
    server.launch()