# Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)
import requests

response1 = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
data1 = response1.json()
sell1 = data1['bid']
buy1 = data1['ask']

response2 = requests.get(
    'https://blockchain.info/ticker')
data2 = response2.json()
sell2 = data2['USD']['sell']
buy2 = data2['USD']['buy']

better_buy = buy1
better_buy_name = 'bitbay.net'
if buy1 > buy2:
    better_buy = buy2
    better_buy_name = 'blockchain.info'

better_sell = sell1
better_sell_name = 'bitbay.net'
if sell1 < sell2:
    better_sell = sell2
    better_sell_name = 'blockchain.info'

print("Currently the ", better_buy_name, "exchange market is better for buying with price", better_buy, ". ",
      better_sell_name, " is better for selling.")
