def make_graph(out_file):
    file = open(out_file, "w")
    for i in range(1, 600, 1):
        if i == 600-1:
            file.write("v" + str(i) + " v1")
        else:
            file.write("v" + str(i) + " v" + str(i+1) + "\n")
    file.close()


make_graph("test11.txt")
