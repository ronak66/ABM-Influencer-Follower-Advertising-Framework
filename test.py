# import python_src.fittingCode.socialModels as sm
# from python_src.Utils import Utils

# G = sm.nearestNeighbor_mod(97134, 0.9, 1)
# # G = sm.randomWalk_mod(97134,0.9,0.23)

# Utils.plot_distribution_networkx(G)

# Code to Measure time taken by program to execute. 
import time 
  
# store starting time 
begin = time.time() 
  

import multiprocessing

def cal(x):
    for i in range(3):
        time.sleep(1)
    return x

a = []

# for i in range(3):
#     l = cal(i)
#     a.append(l)

pool = multiprocessing.Pool(4)
a = pool.map(cal, range(0, 3))


print(a)

end = time.time() 
  
# total time taken 
print(f"Total runtime of the program is {end - begin}") 