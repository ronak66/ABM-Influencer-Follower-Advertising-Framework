class Utils:

    @staticmethod
    def id_degree_file_genrator(filepath,new_filepath):
        id_degree_mp = {}
        with open(filepath) as file:
            for line in file:
                x, y = [int(node_id) for node_id in line.split(' ')]
                if(y in id_degree_mp.keys()):
                    id_degree_mp[y]+=1
                else:
                    id_degree_mp[y]=1
        id_degree_mp = {k: v for k, v in sorted(id_degree_mp.items(), key=lambda item: item[1])}

        with open('{}'.format(new_filepath),"w") as file:
            for node_id in id_degree_mp.keys():
                file.write('{},{}\n'.format(node_id,id_degree_mp[node_id]))

    @staticmethod
    def clean_dataset(filepath,new_filepath):
        a = set()
        with open(filepath) as f:
            for l in f:
                x, y = [int(node_id) for node_id in l.split(' ')]
                a.add((x,y))

        with open("{}".format(new_filepath),"w") as f:
            for i, val in enumerate(a):
                val = list(val)
                f.write(str(val[0]) + " " + str(val[1]) + "\n")

    @staticmethod
    def plot_distribution_networkx(G):
        graph = {}
        for k,v in G.edges:
            if(k in graph.keys()):
                graph[k].append(v)
            else:
                graph[k] = [v]

        d = {}
        for k,v in graph.items():
            if(len(v) in d.keys()):
                d[len(v)]+=1
            else:
                d[len(v)]=1

        for i in G.nodes:
            if(i not in graph.keys()):
                if(0 in d.keys()):
                    d[0]+=1
                else:
                    d[0]=1    
        print(len(list(G.edges)))
        import matplotlib.pyplot as plt
        plt.scatter(list(d.keys()),list(d.values()))
        plt.show()


if __name__ == "__main__":
    # Utils.clean_dataset("/home/ajayrr/Semester7/AI/project/dataset/gplus/gplus_combined.txt", "/home/ajayrr/Semester7/AI/project/ABM-Influencer-Follower-Advertising-Framework/data/cleaned_gplus_combined.txt")
    # Utils.id_degree_file_genrator("/home/ajayrr/Semester7/AI/project/ABM-Influencer-Follower-Advertising-Framework/data/cleaned_gplus_combined.txt", "/home/ajayrr/Semester7/AI/project/ABM-Influencer-Follower-Advertising-Framework/data/gplus_id_degree.txt")
    pass