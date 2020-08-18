import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
import collections

n = int(input('n: '))
k = input('k: ')
G = nx.watts_strogatz_graph(n = int(n), k = int(k), p = 0.5)
d = {}

for i in list(G.edges):
    if(i[0] in d.keys()):
        d[i[0]]+=1
    else:
        d[i[0]]=1
    if(i[1] not in d.keys()):
        d[i[1]]=0

l = {}
for k,v in d.items():
    if(v in l.keys()):
        l[v]+=1
    else:
        l[v]=1
# print(d)
od = collections.OrderedDict(sorted(l.items()))
count=0
for k,v in od.items():
    print(k,v,sep=' -- ')
    count += v
# print(l)
print(count)
plt.plot(np.array(list(od.keys())),np.array(list(od.values())))
plt.xlabel('Out Degree')
plt.ylabel("Number of Nodes")
plt.grid()
plt.show()