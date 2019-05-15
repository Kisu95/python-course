# 3 Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)

import requests
import time
import random


def userBase():
    users = []
    for i in range(100):
        response = requests.get('https://randomuser.me/api/?inc=login,name')
        data = response.json()
        id = i
        username = data['results'][0]['login']['username']
        firstname = data['results'][0]['name']['first']
        lastname = data['results'][0]['name']['last']
        btc = random.random() * 10
        usd = 3000 + (random.random() * 10000)
        user = [id, username, firstname, lastname, btc, usd]
        users.append(user)
        time.sleep(0.01)
    return users


def prices():
    response = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
    data = response.json()
    price = data['ask']
    return price


def transaction(*args, price):
    amount = random.random()
    user1 = (random.randint(0, 99))
    user2 = user1
    while (user1 == user2):
        user2 = random.randint(0, 99)
    user1BTC = args[user1][4]
    user1USD = args[user1][5]
    # print(user1BTC)
    # print(user1USD)
    if amount > user1BTC:
        return print("User don't have enought BTC to exchange.")
    user2USD = args[user2][5]
    user2BTC = args[user2][4]
    if (amount*price) > user2USD:
        return print("User don't have enought USD to exchange.")
    amountusd = amount*price
    user1BTC = user1BTC - amount
    user1USD = user1USD + amountusd
    user2BTC = user2BTC + amount
    user2USD = user2USD - amountusd
    # print(user1BTC)
    # print(user1USD)
    username1 = args[user1][1]
    username2 = args[user2][1]
    return print(username1, " exchanged ", "{0:.3f}".format(amount), " BTC with ",
                 username2, " for ", "{0:.3f}".format(amountusd), " USD.")


users = userBase()
price = prices()

for i in range(5):
    transaction(*users, price=price)
    time.sleep(0.6)
