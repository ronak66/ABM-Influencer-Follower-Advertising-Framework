# Agent Based Model: Influncer-Follower Dynamics for Advertising Campaign

This is the official implementation of [Modeling Influencer Marketing Campaigns In Social Networks](https://arxiv.org/abs/2106.01750).

If you use these resources and methods, please cite the following paper:

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
