
import requests
import json

url = 'https://api.github.com/user/repos'
apiKey = '8c0e5202752a9f00b139b7d0f36bd79f75741975'

response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()

print (response.json())

filename = 'response.json'

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)