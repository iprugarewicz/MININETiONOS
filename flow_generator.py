import json

import requests


class flow_generator:
    data = None
    name = None
    IP = None

    def __init__(self, name, IP):
        self.data = json.loads('{"flows": []}')
        self.name = name
        self.IP = IP

    def add(self, ID, port, DST):
        temp = json.loads('{"priority": 40000}')
        temp.update({"timeout": 0})
        temp.update({"isPermanent": True})
        deviceId = list('0000000000000000')
        deviceId[15] = str(hex(ID)[2])
        temp.update({"deviceId": "of:" + "".join(deviceId)})
        instructions = json.loads('{"type": "OUTPUT","port": "' + str(port) + '"}')
        temp.update({"treatment": ""})
        treatment = json.loads('{"instructions":""}')
        treatment["instructions"] = [instructions]
        temp["treatment"] = treatment
        criteria = json.loads('''
        {"criteria": [{"type": "ETH_DST","mac": 
        "00:00:00:00:00:0''' + hex(DST)[2] + '''"},{"type": "ETH_TYPE",
        "ethType": "0x0800"}]}''')
        temp.update({"selector": ""})
        temp["selector"] = criteria
        self.data["flows"].append(temp)

    #  print("added flow from " + str(ID) + " to " + str(DST) + ", port = " + str(port))

    def __dump(self):
        test = json.dumps(self.data, indent=3)
        with open(self.name + ".json", "w") as file:
            file.write(test)

    def send(self):
        self.__dump()
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', }

        with open(self.name + '.json') as f:
            data = f.read()
            response = requests.post('http://' + self.IP + ':8181/onos/v1/flows', headers=headers, data=data,
                                     auth=('onos', 'rocks'))
        print(response)
