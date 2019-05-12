import requests
import time

users = []

for i in range(100):
    response = requests.get('https://randomuser.me/api/?inc=login,name')
    data = response.json()
    id = i+1
    username = data['results'][0]['login']['username']
    firstname = data['results'][0]['name']['first']
    lastname = data['results'][0]['name']['last']
    user = (id, username, firstname, lastname)
    users.append(user)
    time.sleep(0.1)

print(users)
