import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

dataset = input('Graph (1=gplus or 2=twitter): ')
if(dataset == '1'):
    dataset = 'gplus'
else:
    dataset = 'twitter'
cost = input('Product Cost: ')
interest = input('Interest: ')
path = '../experimental_results/FINAL_RESULTS/Interest_{}_0.2/{}/p{}.csv'.format(interest,dataset,cost)
df = pd.read_csv(path)
x = range(1,7)
y_cac = []
y_cr = []
y1_cac = []
y2_cac = []
y1_cr = []
y2_cr = []
for i in x:
    d = df.loc[df['Influencer Level']==i]
    d1 = d['Buyers']/d['Outreach']
    d = d['Hiring Cost']/d['Buyers']
    y_cac.append(d.mean())
    y1_cac.append(d.mean()-d.std())
    y2_cac.append(d.mean()+ d.std())
    y_cr.append(d1.mean())
    y1_cr.append(d1.mean()-d1.std())
    y2_cr.append(d1.mean()+ d1.std())


ymax = min(y_cac)
xpos = y_cac.index(ymax)
xmax = x[xpos]

plt.figure()
plt.plot(x, y_cac, color='red')
# plt.scatter(x, y_cac, marker='d', color='red', s=100)
plt.scatter(x, y_cac, color='red', s=50)
plt.fill_between(x, y1_cac, y2_cac, color='orange', alpha=0.2)
plt.scatter(x, y1_cac, marker='x', color='red', alpha=0.4)
plt.scatter(x, y2_cac, marker='x', color='red', alpha=0.4)
# plt.annotate('Min CAC', xy=(xmax, ymax), xytext=(xmax-0.5, ymax+(d.std()/2)   ),
#     arrowprops=dict(facecolor='black', shrink=0.05),
# )

plt.grid()
plt.title('Customer Acquisition Cost for willingness={} and graph={}'.format(100-int(cost),dataset))
plt.xlabel('Influence Level')
plt.ylabel('CAC')




plt.figure()
plt.plot(x, y_cr, color='blue')
# plt.scatter(x, y_cr, marker='d', color='red', s=100)
plt.scatter(x, y_cr, color='blue', s=50)
plt.fill_between(x, y1_cr, y2_cr, color='#add8e6', alpha=0.5)
plt.scatter(x, y1_cr, marker='x', color='blue', alpha=0.4)
plt.scatter(x, y2_cr, marker='x', color='blue', alpha=0.4)
# plt.annotate('Min CR', xy=(xmax, ymax), xytext=(xmax-0.5, ymax+(d.std()/2)   ),
#     arrowprops=dict(facecolor='black', shrink=0.05),
# )

plt.grid()
plt.title('Conversion Ratio for willingness={} and graph={}'.format(100-int(cost),dataset))
plt.xlabel('Influence Level')
plt.ylabel('CR')


plt.show()
