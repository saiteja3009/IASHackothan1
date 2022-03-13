import json
import requests

def getsensor(sensor_id):
	with open("config.json", "r") as jsonfile: 
		data = json.load(jsonfile) 
		url = data[sensor_id]['api']
		response = requests.get(url).text
		return json.loads(response)['data']
		
# getsensor("1")
