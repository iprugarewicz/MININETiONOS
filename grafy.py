import csv
import networkx as nx


class graph_from_csv:
    G = None
    n = None
    ports = None

    def __init__(self, file_name):
        self.ports = [[0 for i in range(11)] for j in range(11)]
        self.G = nx.Graph()
        self.__import_graph(file_name)


    def __import_graph(self, file_name):
        graph_data = []
        with open(file_name+".csv", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            for row in enumerate(reader):
                temp = []
                if row[0] == 0:
                    self.n = int(row[1][2])
                else:
                    temp2 = row[1][0].split(",")
                    temp.append(int(temp2[0]))
                    temp.append(int(temp2[1]))
                    temp.append(float(temp2[2]) + 1)
                    temp.append(int(temp2[3]))
                    temp.append(int(temp2[4]))
                    graph_data.append(temp)
        for i in range(1, self.n):
            self.G.add_node(i)
        for i in graph_data:
            self.G.add_edge(i[0], i[1], weight=i[2])
            self.ports[i[0]][i[1]] = int(i[3])
            self.ports[i[1]][i[0]] = int(i[4])

    def shortest_path(self, source, target):
        if self.G.number_of_nodes() == 0:
            print("you need to import graph first")
            return 0
        return nx.dijkstra_path(self.G, source, target)

    def get_ports(self):
        return self.ports
