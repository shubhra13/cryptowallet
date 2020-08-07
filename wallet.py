from constant import *
import subprocess
import json
import os
import pprint
from bit import wif_to_key
from bit import PrivateKeyTestnet
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account
from web3 import Web3
from bit.network import NetworkAPI
from web3.middleware import geth_poa_middleware


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

mnemonic = os.getenv('MNEMONIC', 'federal title audit cause during enlist avocado grape dash spider aspect hawk')
print(mnemonic)
print(type(mnemonic))


def derive_wallets(cointype, mnemonic):

    command = f'php ./derive -g --mnemonic="{mnemonic}" -cols=address,path,privkey,pubkey --coin={cointype} --numderive=3 --format=json'
    print(command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    keys = json.loads(output)    
    return keys


def priv_key_to_account(coin, priv_key):
    """
    This will convert the privkey string in a child key to an account object that bit or web3.py can use to transact
    coin -- the coin type (defined in constants.py).

    priv_key -- the privkey string will be passed through here.
    """
    if (coin == ETH):
        return Account.privateKeyToAccount(priv_key)
    elif (coin == BTCTEST):
        return PrivateKeyTestnet(priv_key)
   
    
def create_tx(coin, account, to, amount):
    """
    this will create the raw, unsigned transaction that contains all metadata needed to transact.
    coin -- the coin type (defined in constants.py).
    account -- the account object from priv_key_to_account.
    to -- the recipient address.
    amount -- the amount of the coin to send.
    """
    if ( coin == ETH):
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    elif(coin == BTCTEST):
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    
def send_tx(coin, account, to , amount):
    """
    This will call create_tx, sign the transaction, then send it to the designated network.
    coin -- the coin type (defined in constants.py).
    account -- the account object from priv_key_to_account.
    to -- the recipient address.
    amount -- the amount of the coin to send.
    """
    if (coin == ETH):
        tx = create_tx(ETH,account, to, amount)
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(result.hex())
        return result.hex()
    elif(coin == BTCTEST):
        tx = create_tx(BTCTEST,account, to, amount)        
        signed_tx = account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx)
    
    
coins = {} #initialize coin object
eth = derive_wallets(ETH, mnemonic) #create ETH accounts
coins[ETH]=eth
btc = derive_wallets(BTCTEST, mnemonic)
coins[BTCTEST]=btc

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(coins)

accountE = priv_key_to_account(ETH, coins[ETH][0]['privkey'])
send_tx(ETH, accountE, "0xc470b0A110C03636d5a6B8821aa34aED59E9f920", 1)

accountB = priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey'])        
send_tx(BTCTEST, accountB, "mjMoK8zFxYaYmQNcG1eUTjtBKWUGAVMorq", 0.00002)

