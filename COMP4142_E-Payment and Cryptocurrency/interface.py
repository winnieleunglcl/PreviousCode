from blockchain import Blockchain
from block import Block
from wallet import Wallets
from transaction import Transaction, coinbase_transaction
from utxo import Utxo

class interface:
    def __init__(self):
        self.wallets = Wallets()
        self.users = dict()
        for user in self.wallets.wallets:
            self.users.update({user["name"]:user["address"]})
        self.user = self.login(self.users.keys())
        self.chain = self.accessChain()
        self.utxo = Utxo()
        self.difficulty = 1
        print("\n\n===== WELCOME TO BETA BLOCKCHAIN SYSTEM =====\n")
        self.printCommandList()

    def login(self,users_name):
        user = ""
        print("Login as...(Alice/Bob/Eve): ")
        user = input()
        users = list(users_name)
        while user not in users:
            print("Existing users: "+str(users)+", please login again:")
            user = input()
        print("Welcome back, "+user)
        print("Your own address: "+self.users[user]+"\n")
        return user
        
    def accessChain(self):
        print("Accessing blockchain...")
        chain = Blockchain(self.users[self.user])
        return chain
    
    def command(self):
        commands = ["1","2","3","4","5"]
        command = input()
        while (command not in commands):
            print("Failed. Please input valid command number:")
            command = input()
        while (command != "5"):
            if command == "1":
                self.chain.print_blockchain()
            if command == "2":
                i,pH,txIds = self.inputBlockInfo()
                #coinbase reward default: 25
                coinbase = coinbase_transaction(self.utxo, self.users[self.user], 25)
                #retrieve all transactions that miner told to add in the block
                txs=self.utxo.findAllTxsWithIds(coinbase, txIds)
                block = Block().set_block(i,pH,self.chain.adjust_difficulty(),txs)
                self.chain.add_block_to_chain(block)
                #new block -> new utxo with all unspent
                self.utxo.newBlockUtxo()
            if command == "3":
                self.printInfo(self.user)
            if command == "4":
                r_address, amount = self.inputTxInfo()
                tx = Transaction().add_transaction(self.utxo, self.users[self.user], r_address, amount)
            print("\n\nOther services needed?")
            self.printCommandList()
            command = input()
        return command
 
    def printCommandList(self):
        print("*----------------------------------------------*")
        print("Available commands:")
        print("1: Check blockchain information")
        print("2: Add a new block")
        print("3: Check wallet info & others' addresses")
        print("4: Perform transaction")
        print("5: Exit system")
        print("*----------------------------------------------*")
        print("\nPlease input command number:")
        command = self.command()
        if (command == "5"):
            print("Exit system. See you next time~")
            exit()

    def printInfo(self, login_user):
        print("")
        self.wallets = Wallets()
        for user in self.wallets.wallets:
            if user["name"] == login_user:
                print("Your name: "+user["name"])
                print("Your address: "+user["address"])
                print("Your balance: "+str(user["balance"])+"\n")
        print("Neighbours' addresses:")
        for user in self.wallets.wallets:
            if user["name"] != login_user:
                print("User name: "+user["name"])
                print("Address: "+user["address"]+"\n")

    def printUtxoTransaction(self):
        self.utxo.printRecords()
    
    def inputBlockInfo(self):
        print("Input block index:")
        index = input()
        index = int(index)
        print("Input previous block hash:")
        prevHash = input()
        #transactions
        self.printUtxoTransaction()
        txids = []
        print("Select transactions to form block - input transaction ids:")
        tx = input()
        txids.append(tx)
        while(tx!="n"):
            print("Continue to input transaction ids, input n to stop:")
            tx = input()
            txids.append(tx)
        return index, prevHash, txids

    def inputTxInfo(self):
        print("Input receiver's address:")
        r_address = input()
        print("Input amount of coins to send:")
        amount = input()
        amount = float(amount)
        return r_address, amount
        
interface()
