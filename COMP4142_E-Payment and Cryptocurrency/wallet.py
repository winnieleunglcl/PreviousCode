from ecdsaKey import keyGen
import json, io, os
from utxo import Utxo

wallets_json = "wallets.json"
READPATH = "./"+wallets_json
CURRENTPATH = "./"

class Wallet:
    def __init__(self, owner_name):
        private_key, public_key, wallet_address = keyGen()
        #for simplicity, as login is needed in this system, an owner_name parameter is here
        self.wallet = self.set_wallet(owner_name,private_key, public_key, wallet_address)
    
    def set_wallet(self, name, private_key, public_key, bitcoin_address):
        wallet = {
            "name":name,
            "private key":private_key,
            "public key":public_key,
            "address":bitcoin_address,
            "balance":0
        }
        return wallet

class Wallets:
    def __init__(self):
        self.wallets = self.checkExistAndRead()
        self.aliceBobAndEve()
        self.updateBalance()

    def checkExistAndRead(self):
        if os.path.isfile(READPATH) and os.access(READPATH, os.R_OK):
            with open(wallets_json) as file:
                data = json.load(file)
            return data
        else:
            with io.open(os.path.join(CURRENTPATH, wallets_json), 'w') as db_file:
                db_file.write(json.dumps([]))
            with open(wallets_json) as file:
                data = json.load(file)            
            return data
        
    def append(self, wallet):
        with open(wallets_json) as file:
            data = json.load(file)
        data.append(wallet)
        with open(wallets_json, 'w') as json_file:
            json.dump(data, json_file,indent=4,separators=(',',': '))

    def getPublicKey(self, address):
        public_key = None
        with open(wallets_json) as file:
            data = json.load(file)
        for wallet in data:
            if wallet["address"] == address:
                public_key = wallet["public key"]
        return public_key

    def getPrivateKey(self, s_address):
        private_key = None
        with open(wallets_json) as file:
            data = json.load(file)
        for wallet in data:
            if wallet["address"] == s_address:
                private_key = wallet["private key"]
        return private_key

    def checkReceiverExist(self, receiver_address):
        exist = False
        with open(wallets_json) as file:
            data = json.load(file)
        for wallet in data:
            if wallet["address"] == receiver_address:
                exist = True
        return exist

    def updateBalance(self):
        utxo = Utxo()
        new_wallets = []
        with open(wallets_json) as file:
            data = json.load(file)
        for wallet in data:
            all_unspent, balance = utxo.findSenderUnspent(wallet["address"])
            wallet.update({"balance":balance})
            new_wallets.append(wallet)
        with open(wallets_json, 'w') as json_file:
            json.dump(new_wallets, json_file,indent=4,separators=(',',': '))

    def getBalance(self, s_address):
        self.updateBalance()
        balance = 0.0
        with open(wallets_json) as file:
            data = json.load(file)
        for wallet in data:
            if wallet["address"] == s_address:
                balance = wallet["balance"]
        return balance

#for simplicity, we only got Alice, Bob and Eve as users in this system, initialize and store their wallets
    def aliceBobAndEve(self):
        if (len(self.wallets)==0):
            self.append(Wallet("Alice").wallet)
            self.append(Wallet("Bob").wallet)
            self.append(Wallet("Eve").wallet)
