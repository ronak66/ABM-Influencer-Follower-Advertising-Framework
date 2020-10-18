import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

dataset = input('Graph (gplus or twitter): ')
cost = input('Product Cost: ')
interest = input('Interest: ')
path = '../experimental_results/FINAL_RESULTS/Interest_{}_0.2/{}/p{}.csv'.format(interest,dataset,cost)
df = pd.read_csv(path)
x = range(1,7)
y = []
y1 = []
y2 = []
for i in x:
    d = df.loc[df['Influencer Level']==i]
    d = d['Hiring Cost']/d['Buyers']
    y.append(d.mean())
    y1.append(d.mean()-d.std())
    y2.append(d.mean()+ d.std())


plt.plot(x, y, color='red')
# plt.scatter(x, y, marker='d', color='red', s=100)
plt.scatter(x, y, color='red', s=50)
plt.fill_between(x, y1, y2, color='orange', alpha=0.4)
plt.scatter(x, y1, marker='x', color='red', alpha=0.3)
plt.scatter(x, y2, marker='x', color='red', alpha=0.3)

plt.grid()
plt.title('Customer Acquisition Cost for willingness={} and graph={}'.format(100-int(cost),dataset))
plt.xlabel('Influence Level')
plt.ylabel('CAC')
plt.show()
