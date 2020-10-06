from Graph import Graph, Edge
from InfluencerAgent import InfluencerAgent
from InfluencerAdvertisingModel import InfluencerAdvertisingModel

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer

import random
from Utils import Utils

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
    return portrayal


def display(graph_type):
    chart1 = ChartModule(
        [{"Label": "No who bought",
        "Color": "Black"}],
        data_collector_name='datacollector'
    )
    chart2 = ChartModule(
        [{"Label": "No bought at every timestep",
        "Color": "Black"}],
        data_collector_name='datacollector'
    )
    if(graph_type=='networkx'):
        grid = CanvasGrid(agent_portrayal, width, height, 500, 500)
        return [grid,chart1,chart2]
    return [chart1,chart2]

def get_node_ids_inRange(filepath, x, y):
    node_ids = []
    outdegrees = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            id = int(line[0])
            outDegree = int(line[1])

            if outDegree >= x and outDegree <=y:
                node_ids.append(id)
                outdegrees.append(outDegree)
    return node_ids, outdegrees

def choose_random_advertisers(node_ids, outdegrees, n, sort=0):
    advertiser_list = []
    advertiser_outdegrees = []
    idx = random.sample(range(0, len(node_ids)), n)

    if(sort==1):
        sorted_ids_wrt_outdegree = [x for _,x in sorted(zip(outdegrees,node_ids))]
        sorted_outdegree = [y for y,_ in sorted(zip(outdegrees,node_ids))]
        return sorted_ids_wrt_outdegree[-n:], sorted_outdegree[-n:]

    for i in idx:
        advertiser_list.append(node_ids[i])
        advertiser_outdegrees.append(outdegrees[i])
    return advertiser_list, advertiser_outdegrees

def choose_advertisers_with_HiringConstraint(node_ids, outdegrees, total_hiring_cost):
    cost_per_post_per_follower = 0.01
    hiring_cost = 0
    advertiser_list = []
    advertiser_outdegrees = []

    sorted_ids_wrt_outdegree = [x for _,x in sorted(zip(outdegrees,node_ids))]
    sorted_outdegree = [y for y,_ in sorted(zip(outdegrees,node_ids))]
    idx = random.sample(range(0, len(node_ids)), len(node_ids))

    i=0;
    while(i<len(idx)):
        hiring_cost += sorted_outdegree[idx[i]]*cost_per_post_per_follower
        if hiring_cost > total_hiring_cost:
            if i == len(idx) - 1:
                print(i,len(idx)-1)
                break
            else:
                i += 1
                continue

        advertiser_list.append(sorted_ids_wrt_outdegree[idx[i]])
        advertiser_outdegrees.append(sorted_outdegree[idx[i]])
        i += 1
    print(i)
    return advertiser_list, advertiser_outdegrees

def choose_best_advertisers_with_HiringConstraint(node_ids, outdegrees, total_hiring_cost):
    cost_per_post_per_follower = 0.01
    hiring_cost = 0
    advertiser_list = []
    advertiser_outdegrees = []

    sorted_ids_wrt_outdegree = [x for _,x in sorted(zip(outdegrees,node_ids))]
    sorted_outdegree = [y for y,_ in sorted(zip(outdegrees,node_ids))]
    i=1;
    while(hiring_cost < total_hiring_cost):
        hiring_cost += sorted_outdegree[-i]*cost_per_post_per_follower
        if hiring_cost > total_hiring_cost:
            break
        advertiser_list.append(sorted_ids_wrt_outdegree[-i])
        advertiser_outdegrees.append(sorted_outdegree[-i])
        i += 1
    return advertiser_list, advertiser_outdegrees

if __name__ == '__main__':

    width = height = 50
    number_of_nodes = width*height
    # graph_type='twitter'
    graph_type='networkx'
    # graph_type = 'synthetic'

    if(graph_type=='networkx'):
        node_ids = {
            1: [1]
        }
        grid=0
        graph = Graph()
        graph.create_networkx_graph(9705668, 0.9, 5)
        Utils.generate_graph_txt(graph)
        Utils.plot_distribution_networkx(graph)

    if (graph_type=='synthetic'):

        node_ids_inRange, outdegrees = get_node_ids_inRange("../data/synthetic_network_id_degree.txt", 701, 750)
        max_advertiser_list = []
        max_hiring_cost = 0
        for _ in range(100):
            advertiser_list, advertiser_outdegrees = choose_advertisers_with_HiringConstraint(node_ids_inRange, outdegrees, 30)
            hiring_cost = sum(advertiser_outdegrees)*0.01
            if(hiring_cost > max_hiring_cost):
                max_advertiser_list = advertiser_list
                max_hiring_cost = hiring_cost

        advertiser_list = max_advertiser_list
        print("Advertiser nodes: ", advertiser_list, "Number of advertisers: ", len(advertiser_list), "\nTotal out degree: ", sum(advertiser_outdegrees))
        node_ids = {
            1: advertiser_list
        }
        grid=0
        graph = Graph()
        graph.create_twitter_graph(filepath='../data/synthetic_network.txt')

    if(graph_type=='twitter'):
        node_ids_inRange, outdegrees = get_node_ids_inRange("../data/twitter_id_degree.txt", 3001, 3500)
        # advertiser_list, advertiser_outdegrees = choose_random_advertisers(node_ids_inRange, outdegrees, 10, sort=0)
        max_advertiser_list = []
        max_advertiser_outdegrees = []
        max_hiring_cost = 0
        for _ in range(100):
            advertiser_list, advertiser_outdegrees = choose_advertisers_with_HiringConstraint(node_ids_inRange, outdegrees, 30)
            hiring_cost = sum(advertiser_outdegrees)*0.01
            if(hiring_cost > max_hiring_cost):
                max_advertiser_list = advertiser_list
                max_hiring_cost = hiring_cost
                max_advertiser_outdegrees = advertiser_outdegrees

        advertiser_list = max_advertiser_list
        advertiser_outdegrees = max_advertiser_outdegrees
        print("Advertiser nodes: ", advertiser_list, "Number of advertisers: ", len(advertiser_list), "\nTotal out degree: ", sum(advertiser_outdegrees))
        node_ids = {
            1: advertiser_list
        }
        grid=0
        graph = Graph()
        graph.create_twitter_graph(filepath='../data/cleaned_gplus_combined.txt')
    
    if(graph_type=='gplus'):
        node_ids_inRange, outdegrees = get_node_ids_inRange("../data/gplus_id_degree.txt", 3001, 3500)
        # advertiser_list, advertiser_outdegrees = choose_random_advertisers(node_ids_inRange, outdegrees, 10, sort=0)
        advertiser_list, advertiser_outdegrees = choose_advertisers_with_HiringConstraint(node_ids_inRange, outdegrees, 68)
        print("Advertiser nodes: ", advertiser_list, "Number of advertisers: ", len(advertiser_list), "\nTotal out degree: ", sum(advertiser_outdegrees))
        node_ids = {
            1: advertiser_list
            # 1:[115485051]
        }
        grid=0
        graph = Graph()
        graph.create_twitter_graph(filepath='../data/cleaned_gplus_combined.txt')

    # params = {
    #     "width":width,
    #     "height":height,
    #     "Graph": graph,
    #     "node_ids": node_ids,
    #     "grid": grid,
    #     "product_cost": 10,
    #     "hiring_budget": 30
    # }
    #
    # server = ModularServer(
    #     InfluencerAdvertisingModel,
    #     display(graph_type),
    #     "Influencer Advertising Model",
    #     params
    # )
    # server.port = 8521
    # server.launch()
