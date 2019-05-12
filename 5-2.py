# Use https: // randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)
import requests
import time


class User:
    def __init__(self, id, username, firstname, lastname):
        self.id = id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname


users = []

for i in range(100):
    response = requests.get('https://randomuser.me/api/?inc=login,name')
    data = response.json()
    id = i+1
    username = data['results'][0]['login']['username']
    firstname = data['results'][0]['name']['first']
    lastname = data['results'][0]['name']['last']
    users.append(User(id, username, firstname, lastname))
    time.sleep(0.1)

print(users)
