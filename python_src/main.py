from Graph import Graph, Edge
from InfluencerAgent import InfluencerAgent
from InfluencerAdvertisingModel import InfluencerAdvertisingModel

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}

    if(agent.hired == True):
        portrayal["Color"] = "blue"
    else:
        if(agent.decision == True):
            portrayal["Color"] = "green"
            portrayal["r"] = 0.2
    # if agent.wealth > 0:
    #     if(agent.start == 1):
    #         portrayal["Color"] = "blue"
    #         portrayal["Layer"] = 0
    #     else:
    #         portrayal["Color"] = "red"
    #         portrayal["Layer"] = 0
    # else:
    #     portrayal["Color"] = "green"
    #     portrayal["Layer"] = 1
    #     portrayal["r"] = 0.2
    return portrayal

if __name__ == '__main__':
    width = height = 50
    number_of_nodes = width*height
    graph = Graph(number_of_nodes,100)
    grid = CanvasGrid(agent_portrayal, width, height, 500, 500)
    # grid = NetworkModule(agent_portrayal)
    server = ModularServer(InfluencerAdvertisingModel,
                    [grid],
                    "Influencer Advertising Model",
                    {"width":width, "height":height, "Graph": graph, "node_ids": [1,2,3]})
    server.port = 8521 # The default
    server.launch()