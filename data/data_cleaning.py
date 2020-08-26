def clean(file_path):
    a = set()
    with open(file_path) as f:
        for l in f:
            x, y = [int(node_id) for node_id in l.split(' ')]
            a.add((x,y))

    with open("cleaned_{}".format(file_path),"w") as f:
        for i, val in enumerate(a):
            val = list(val)
            f.write(str(val[0]) + " " + str(val[1]) + "\n")


if __name__ == '__main__':
    clean('twitter_combined.txt')