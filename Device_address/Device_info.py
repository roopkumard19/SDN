import requests
global data
def address():
	global data
	result = requests.get("http://localhost:8080/wm/device/")
	data = result.json()
	print "1st host mac", data["devices"][0]["mac"]
	print "2nd host mac", data["devices"][1]["mac"]
	print "1st host ip ", data["devices"][0]["ipv4"]
	print "1st host ip ", data["devices"][1]["ipv4"]

address()
