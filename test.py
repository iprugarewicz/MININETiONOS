import controller as c

test = c.controller("flows", "sweden_map", "192.168.0.29")
test.generate_flows(5, 3, 120)
