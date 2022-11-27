import csv
import networkx as nx


class graph_from_csv:
    G = None
    n = None
    ports = None
    bandwidths = None

    def __init__(self, file_name):
        self.ports = [[0 for _ in range(11)] for _ in range(11)]
        self.bandwidths = [[0 for _ in range(11)] for _ in range(11)]
        self.G = nx.Graph()
        self.__import_graph(file_name)

    def __import_graph(self, file_name):
        graph_data = []
        with open(file_name + ".csv", newline='') as csvfile:
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
                    temp.append(int(temp2[5]))
                    graph_data.append(temp)
        for i in range(1, self.n):
            self.G.add_node(i)
        for i in graph_data:
            self.G.add_edge(i[0], i[1], weight=i[2])
            self.ports[i[0]][i[1]] = int(i[3])
            self.ports[i[1]][i[0]] = int(i[4])
            self.bandwidths[i[0]][i[1]] = int(i[5])
            self.bandwidths[i[1]][i[0]] = int(i[5])

    def shortest_path(self, source, target, bw):
        G = self.G
        bandwidths = self.bandwidths
        if self.G.number_of_nodes() == 0:
            print("you need to import graph first")
            return 0
        found = False
        trace_history = []
        trace = None
        bw_supplied = True
        while not found:
            trace = nx.dijkstra_path(G, source, target)
            if trace in trace_history:
                if trace != trace_history[0]:
                    bw_supplied = True
                found = True
            trace_history.append(trace)

            for i in range(len(trace) - 1):
                if bandwidths[trace[i]][trace[i + 1]] < bw:
                    bw_supplied = False
                    n: dict = G.get_edge_data(trace[i], trace[i + 1])
                    G.add_edge(trace[i], trace[i + 1], weight=n['weight'] + 1000)
                    break

        print("final trace: ", trace)
        if not bw_supplied:
            print("Unfortunately it isn't possible to supply required bandwidth")
        return trace

    def get_ports(self):
        return self.ports
