import json

with open('t_config.json', 'r+') as f:
	data = json.load(f)
	for server in data:
		data[server]['aliases'] = {}
		data[server]['selfroles'] = []

with open('t_config.json', 'w') as f:
	
	f.write(json.dumps(data, indent=4, sort_keys=True))

