class Utils:

    @staticmethod
    def id_degree_file_genrator(filepath,dataset_name):
        id_degree_mp = {}
        with open(filepath) as file:
            for line in file:
                x, y = [int(node_id) for node_id in line.split(' ')]
                if(y in id_degree_mp.keys()):
                    id_degree_mp[y]+=1
                else:
                    id_degree_mp[y]=1
        id_degree_mp = {k: v for k, v in sorted(id_degree_mp.items(), key=lambda item: item[1])}

        with open('{}_id_degree.txt'.format(dataset_name),"w") as file:
            for node_id in id_degree_mp.keys():
                file.write('{},{}\n'.format(node_id,id_degree_mp[node_id]))


