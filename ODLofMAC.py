import httplib2
import json

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')
resp, content = h.request('http://127.0.0.1:8181/restconf/operational/network-topology:network-topology/topology/flow:1/', "GET")
allFlowStats = json.loads(content)
for i in allFlowStats['topology']:
	for j in i:
		if j == 'topology-id':
			print i[j]
