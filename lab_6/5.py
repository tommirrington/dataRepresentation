import requests, json
import pandas

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()
#print(data)



#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
	json.dump(data, f, indent=4)


#print(type(response))
pandas.read_json("githubusers.json").to_excel("output.xlsx")