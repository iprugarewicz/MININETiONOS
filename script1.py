import requests
from requests.auth import HTTPBasicAuth

onosIp = "http://192.168.0.237:8181/onos/v1/"

r = requests.delete(onosIp + "flows/application/org.onosproject.rest", auth=HTTPBasicAuth("onos","rocks"))

print(r.status_code)
