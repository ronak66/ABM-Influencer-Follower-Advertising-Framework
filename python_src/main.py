from Graph import Graph, Edge
from InfluencerAgent import InfluencerAgent
from InfluencerAdvertisingModel import InfluencerAdvertisingModel

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer

import random


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

def choose_random_advertisers(node_ids, outdegrees, n):
    advertiser_list = []
    advertiser_outdegrees = []
    idx = random.sample(range(0, len(node_ids)), n)

    for i in idx:
        advertiser_list.append(node_ids[i])
        advertiser_outdegrees.append(outdegrees[i])
    return advertiser_list, advertiser_outdegrees

if __name__ == '__main__':

    ll = [20293613, 57026351, 243079375, 171154131, 15810838, 40974224, 14861285, 10257492, 58930815, 15080671, 92899083, 16135047, 15745674, 169496268, 246500501, 58886037, 16803196, 138530516, 54086230, 319576850, 174540176, 265810013, 24239440, 280629993, 15291335, 9822052, 96994187, 211303345, 18089255, 352828674, 15101693, 361396896, 305364977, 2569261, 53792610, 86300007, 209799012, 19469676, 25541185, 24511456, 268425888, 25948843, 216476063, 15826432, 190388631, 130665252, 243013128, 200127090, 271044958, 324151971, 18952294, 61445012, 14069676, 20449133, 17843236, 15075834, 259763895, 17704895, 21575175, 319459265, 81424707, 144284168, 5680622, 45609049, 191613738, 216030263, 15205995, 277152703, 13761042, 43821761, 15147042, 59168805, 163802710, 63307960, 177264696, 381565337, 406668148, 149680765, 126412041, 109550381, 14298557, 83665015, 282860504, 705663, 9984332, 266941320, 15032882, 19109172, 123348683, 17659206, 48564118, 61356546, 69147333, 13598222, 282484132, 23407381, 422168320, 12069912, 97477051, 34041607, 189158296, 190969105, 21536398, 13085462, 24056199]


    width = height = 50
    number_of_nodes = width*height
    graph_type='twitter'
    # graph_type='networkx'

    if(graph_type=='networkx'):
        node_ids = {
            1: [1]
        }
        grid=1
        graph = Graph()
        graph.create_networkx_graph(n=number_of_nodes, k=250)

    if(graph_type=='twitter'):
        # node_ids = [89634510] # outdergree 20
        # node_ids = [115485051] # outdergree 3383
        # node_ids = [115485051, 40981798] # outdergree 3383 and 3216
        # node_ids = [16157855] # outdergree 157
        # node_ids = [14155052] # outdergree 342
        # node_ids = [144040563] # outdergree 628
        # node_ids = [40981798] #outdegree 3216

        node_ids_inRange, outdegrees = get_node_ids_inRange("../data/twitter_id_degree.txt", 1, 50)
        advertiser_list, advertiser_outdegrees = choose_random_advertisers(node_ids_inRange, outdegrees, 40)
        print("Advertiser nodes: ", advertiser_list, "Total out degree: ", sum(advertiser_outdegrees))
        node_ids = {
            # 1:  [115485051] #1 advertiser


            # 1: [16303106, 3359851]      #2 advertisers

             # 1:[27633075, 79797834, 14654965]     #3 advertisers

            # 1:[96848570, 259379883, 807095, 15666380, 116036694]      #5 advertisers

            # 1:[180505807, 7872262, 18963070, 131029775, 46220856, 61853389, 8295072, 20291791, 51263592, 52758395]    #10 advertisers

            # 1:[325830217, 36008570, 19081001, 14856951, 15937155, 21224647, 37077041, 110826948, 15665127, 9423662, 143381041, 54991635, 23996836, 386064033, 335071071, 2960721, 397067160, 14993689, 16237246, 214201922, 156349747, 15717356, 151759225, 18269449, 32032000, 108298982, 57875811, 17001435, 4398351, 15112249, 15578561, 673123, 16475403, 60201129, 90942642, 200713206, 19658506, 283747772, 15310917, 20999409, 9796452, 306472866, 34947001, 30957246, 213849301, 666043, 162442852, 24844163, 15947602, 18622869]  #50 advertisers

            # 1:[59416333, 60642052, 9279652, 124592937, 36041817, 1585, 44705716, 3299561, 366472553, 261171156, 19186071, 17030680, 276905731, 37008705, 25527966, 24278900, 13797612, 171969696, 19948202, 14637048, 16843806, 91517656, 15851057, 82623694, 108746742, 44449776, 66532400, 65360193, 36256788, 14287094, 344951019, 14888217, 269085895, 813491, 127503320, 23275004, 35012277, 237335431, 17417402, 34722669, 14273705, 978241, 23480504, 19662799, 15696404, 118485945, 19178827, 170002037, 222672936, 129939387, 389486164, 403101513, 14838379, 12712332, 39164092, 158126576, 220813988, 103944265, 41402578, 32652567, 16951769, 552121630, 16669898, 236657680, 17810432, 36771809, 46322933, 86799233, 14167197, 231931886, 199370728, 39163475, 3526, 18131039, 45609049, 34041607, 87038861, 14830184, 78661203, 186470618, 45524837, 312285643, 73395703, 41693, 213171360, 150172935, 14880616, 105531612, 39693835, 58083306, 16792916, 175561847, 21024997, 16416378, 14307102, 240393947, 10971502, 100826213, 247520516, 33174357]


            1: advertiser_list

        }


        grid=0
        graph = Graph()
        graph.create_twitter_graph(filepath='../data/cleaned_twitter_combined.txt')

    if(graph_type=='gplus'):

        node_ids = {
            1: [111091089527727420853] #outdegree 17055
        }

        grid=0
        graph = Graph()
        graph.create_twitter_graph(filepath='../data/cleaned_gplus_combined.txt')

    params = {
        "width":width,
        "height":height,
        "Graph": graph,
        "node_ids": node_ids,
        "grid": grid,
        "product_cost": 10,
        "hiring_budget": 200
    }

    server = ModularServer(
        InfluencerAdvertisingModel,
        display(graph_type),
        "Influencer Advertising Model",
        params
    )
    server.port = 8521
    server.launch()
