<h1 align="center">
  <br>
  [arXiv] Modeling Influencer Marketing Campaigns In Social Networks
  <br>
</h1>
  <p align="center">
    <a href="https://ronak66.github.io/">Ronak Doshi</a> •
    <a href="https://aj-rr.github.io/">Ajay Ramesh Ranganathan</a> •
    <a href="https://www.iiitb.ac.in/faculty/shrisha-rao">Shrisha Rao</a>
  </p>
<h4 align="center">Official repository of the paper</h4>




# Paper

> **Modeling Influencer Marketing Campaigns In Social Networks**<br>
> Ronak Doshi, Ajay Ramesh Ranganathan, Shrisha Rao<br>
>
> **Abstract:** *Social media is extensively used in today’s world. It facilitates quick and easy sharing of information which makes it a good medium to advertize products. Influencers of a social media network, owing to their massive popularity, provide a huge potential customer base. However, it is not straightforward to decide which influencers should be selected for an advertizing campaign that can generate high returns with low investment. In this work, we present an agent-based model (ABM) that can simulate the dynamics of influencer advertizing campaigns in a variety of scenarios and can help to discover the best influencer marketing strategy. Our system is a probabilistic graph-based model that provides the additional advantage to incorporate real-world factors such as customers’ interest in a product, customer behavior, the willingness to pay, a brand’s investment cap, influencers’ engagement with influence diffusion, and the nature of the product being advertized viz. luxury and non-luxury. Using customer acquisition cost and conversion ratio as a unit economic, we evaluate the performance of different kinds of influencers under a variety of circumstances that are simulated by varying the nature of the product and the customers’ interest. Our results exemplify the circumstance-dependent nature of influencer marketing and provide insight into which kinds of influencers would be a better strategy under respective circumstances. For instance, we show that as the nature of the product varies from luxury to non-luxury, the performance of celebrities declines whereas the performance of nano-influencers improves. In terms of the customers’ interest, we find that the performance of nano-influencers declines with the decrease in customers’ interest whereas the performance of celebrities improves.*

## Citation
* Ronak Doshi, Ajay Ramesh Ranganathan, & Shrisha Rao. (2021). Modeling Influencer Marketing Campaigns In Social Networks.*, 2021. 
```
@misc{doshi2021modeling,
      title={Modeling Influencer Marketing Campaigns In Social Networks}, 
      author={Ronak Doshi and Ajay Ramesh Ranganathan and Shrisha Rao},
      year={2021},
      eprint={2106.01750},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
<h4 align="center">preprint on arXiv: <a href="https://arxiv.org/abs/2106.01750">2106.01750</a></h4>



## Run Locally
**1. Clone the repo**
```
$ git https://github.com/ronak66/ABM-Influencer-Follower-Advertising-Framework.git 
$ cd ABM-Influencer-Follower-Advertising-Framework 
```
**2. Install and Create a Virtual Environment (If already installed, skip 1st command)**    
```
$ python3 -m pip install --user virtualenv
$ python3 -m venv env
$ source env/bin/activate
```
**3. Install all the required dependencies**    
```
$ pip3 install -r requirements.txt
```
**4. Run the system**  
```
$ python3 python_src/main.py
```
