import httplib2
import json
 
h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')
 
URL = 'http://127.0.0.1:8181/restconf/operations/snmp:snmp-get'
 
Param = {
            "input":
                    {
                        "ip-address": "127.0.0.1",
                        "oid" : "1.3.6.1.2.1.1.6.0",
                        "get-type" : "GET",
                        "community" : "public"
    }
}
 
resp, content = h.request(
    uri = URL,
    method = 'POST',
    headers={'Content-Type':'application/json'},
    body=json.dumps(Param)
    )
 
Info = json.loads(content)
 
count = len(Info['output']['results'])
 
print resp
 
for i in range(count):
    print 'OID\t\t\t\t\t\tValue'
    print Info['output']['results'][i]['oid'],'\t\t',Info['output']['results'][i]['value']
