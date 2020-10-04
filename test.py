import python_src.fittingCode.socialModels as sm
from python_src.Utils import Utils

G = sm.nearestNeighbor_mod(97134, 0.9, 1)
# G = sm.randomWalk_mod(97134,0.9,0.23)

Utils.plot_distribution_networkx(G)