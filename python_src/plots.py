import matplotlib.pyplot as plt
import numpy as np

def plot_numAdvert_buyers(filepath):
    data = np.genfromtxt(filepath, delimiter=",", names=["num_advert", "buyers", "outreach"])
    fig,ax = plt.subplots()
    ax.plot(data["num_advert"], data["buyers"], color="red")
    ax.set_xlabel("Number of Advertizers")
    ax.set_ylabel("Number of Buyers", color="red")

    ax2 = ax.twinx()
    ax2.plot(data["num_advert"], data["outreach"], color="blue")
    ax2.set_ylabel("Number of Agents Reached", color="blue")
    fig.savefig('../experimental_results/num_advertsVsBuyers/num_advertisersVsbuyers.jpeg', format='jpeg', bbox_inches = 'tight')

if __name__ == "__main__":
    plot_numAdvert_buyers("../data/AdvertiserNumberVsBuyers.csv")
