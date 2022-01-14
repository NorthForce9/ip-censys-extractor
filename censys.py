import requests,sys,json

per_page = sys.argv[2]
next_page = sys.argv[3]
qeury = sys.argv[1]

url = ('https://search.censys.io/api/v2/hosts/search?q='+qeury+'&per_page='+per_page+'&virtual_hosts=EXCLUDE')
heders = {
	'accept': 'application/json',
	'Authorization': 'Basic NTI5ZDZmODAtMjI3NS00NDFmLWE3YzMtZTJkZDc4MWJiYWIxOnhtbHdjVGdKOXFGT1ZKYXhJcGhNZHZUSmtkY2tya3Za'
}
data = requests.get(url,headers=heders)
json_object = json.loads(data.text)

qorser = json_object['result']['links']['next']
for result in json_object['result']['hits']:
		print(result["ip"])
for i in next_page:

	url = ('https://search.censys.io/api/v2/hosts/search?q='+qeury+'&per_page='+per_page+'&virtual_hosts=EXCLUDE&cursor='+qorser)
	heders = {
		'accept': 'application/json',
		'Authorization': 'Basic NTI5ZDZmODAtMjI3NS00NDFmLWE3YzMtZTJkZDc4MWJiYWIxOnhtbHdjVGdKOXFGT1ZKYXhJcGhNZHZUSmtkY2tya3Za'
	}
	data2 = requests.get(url,headers=heders)
	json_object = json.loads(data2.text)
	qorser = json_object['result']['links']['next']

	for result in json_object['result']['hits']:
		print(result["ip"])


# woohoooooooo i make it 



