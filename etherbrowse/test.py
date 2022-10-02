import config 
from pprint import pprint 
from web3 import Web3


# HTTPProvider - connect to Ethereum node via infura
w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

print(w3.eth.block_number)

balance = w3.eth.get_balance("0xdfDf2D882D9ebce6c7EAc3DA9AB66cbfDa263781")

print(balance)

ether_balance = w3.fromWei(balance, 'ether')

print(ether_balance)

transaction = w3.eth.get_transaction("0x7bd6c29656092d6dc108c738219d78c08998b3f5b39c03eee5d2667ea48d3d2a")

pprint(transaction, depth=1, indent=4)
