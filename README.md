<h1 align="center">
  <br>
  <a href="https://ieeexplore.ieee.org/document/9689053" >[IEEE Transactions] Modeling Influencer Marketing Campaigns In Social Networks
  <br></a>
</h1>
  <p align="center">
    <a href="https://ronak66.github.io/">Ronak Doshi</a> •
    <a href="https://aj-rr.github.io/">Ajay Ramesh Ranganathan</a> •
    <a href="https://www.iiitb.ac.in/faculty/shrisha-rao">Shrisha Rao</a>
  </p>
<h4 align="center">Official repository of the paper</h4>




# Paper

> **Title**: *Modeling Influencer Marketing Campaigns In Social Networks*  
> **Authors**: *Ronak Doshi, Ajay Ramesh Ranganathan, Shrisha Rao*  
> **Published in**: *IEEE Transactions on Computational Social Systems*
>
> **Abstract:** *Social media are extensively used in today's world, and facilitate quick and easy sharing of information, which makes them a good way to advertise products. Influencers of a social media network, owing to their massive popularity, provide a huge potential customer base. However, it is not straightforward to decide which influencers should be selected for an advertising campaign that can generate high returns with low investment. In this work, we present an agent-based model (ABM) that can simulate the dynamics of influencer advertising campaigns in a variety of scenarios and can help discover the best influencer marketing strategy. Our system is a probabilistic graph-based model that provides the additional advantage to incorporate real-world factors such as customers' interest in a product, customer behavior, the willingness to pay, a brand's investment cap, influencers' engagement with influence diffusion, and the nature of the product being advertised, viz. luxury and non-luxury. Using customer acquisition cost and conversion ratio as a unit economic, we evaluate the performance of different kinds of influencers under a variety of circumstances that are simulated by varying the nature of the product and the customers' interest. Our results exemplify the circumstance-dependent nature of influencer marketing and provide insights into which kinds of influencers would be a better strategy under respective circumstances. For instance, we show that as the nature of the product varies from luxury to non-luxury, the performance of celebrities declines, whereas the performance of nano-influencers improves. In terms of the customers' interest, we find that the performance of nano-influencers declines with the decrease in customers' interest, whereas the performance of celebrities improves.*

## Citation
*R. Doshi, A. Ramesh and S. Rao, "Modeling Influencer Marketing Campaigns in Social Networks," in IEEE Transactions on Computational Social Systems, doi: 10.1109/TCSS.2022.3140779.*, 2022. 
```
@ARTICLE{9689053,  
  author={Doshi, Ronak and Ramesh, Ajay and Rao, Shrisha},  
  journal={IEEE Transactions on Computational Social Systems},   
  title={Modeling Influencer Marketing Campaigns in Social Networks},   
  year={2022},  
  volume={},  
  number={},  
  pages={1-13},  
  doi={10.1109/TCSS.2022.3140779}
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
