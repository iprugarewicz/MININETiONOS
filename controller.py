import grafy as g
import flow_generator as f


class controller:
    graph = None
    flow = None
    ports = []

    def __init__(self, json_name, csv_name, IP):
        self.graph = g.graph_from_csv(csv_name)
        self.flow = f.flow_generator(json_name, IP)
        self.ports = self.graph.get_ports()

    def generate_flows(self, A, B):
        trace = self.graph.shortest_path(A, B)
        self.flow.add(A, 1, A)
        self.flow.add(B, 1, B)
        for i in range(len(trace) - 1):
            print(trace[i], trace[i + 1],
                  self.ports[trace[i]][trace[i + 1]], self.ports[trace[i + 1]][trace[i]])
            self.flow.add(trace[i], self.ports[trace[i]][trace[i + 1]], B)
            self.flow.add(trace[i + 1], self.ports[trace[i + 1]][trace[i]], A)

    def send(self):
        self.flow.send()

    def generate_and_send(self,A,B):
        self.generate_flows(A,B)
        self.send()
