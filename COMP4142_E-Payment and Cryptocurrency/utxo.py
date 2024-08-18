import json, io, os

utxo_json = "utxo.json"
READPATH = "./"+utxo_json
CURRENTPATH = "./"

class Utxo:
    def __init__(self):
        self.utxo = self.checkExistAndRead()

    def checkExistAndRead(self):
        if os.path.isfile(READPATH) and os.access(READPATH, os.R_OK):
            with open(utxo_json) as file:
                data = json.load(file)
            return data
        else:
            with io.open(os.path.join(CURRENTPATH, utxo_json), 'w') as db_file:
                db_file.write(json.dumps([]))
            with open(utxo_json) as file:
                data = json.load(file)            
            return data
        
    def appendUtxoRecord(self, transaction):
        with open(utxo_json) as file:
            data = json.load(file)
        #if p2pkh verified -> unspent -> add to utxo
        data.append(transaction)
        with open(utxo_json, 'w') as json_file:
            json.dump(data, json_file,indent=4,separators=(',',': '))

    def newBlockUtxo(self):
        all_unspent = self.findAllUnspent()
        with io.open(os.path.join(CURRENTPATH, utxo_json), 'w') as db_file:
            db_file.write(json.dumps([]))
        with open(utxo_json) as file:
            data = json.load(file)
        for tx in all_unspent:
            self.appendUtxoRecord(tx)
        
    def findAllTxsWithIds(self, coinbase, txids):
        txs = []
        with open(utxo_json) as file:
            data = json.load(file)
        txs.append(coinbase)
        for tx in data:
            if tx[2][0] in txids:
                txs.append(tx)
        return txs
            
    def findAllUnspent(self):
        all_unspent = []
        with open(utxo_json) as file:
            data = json.load(file)
        for tx in data:
            for i in range(len(tx[1])):
                if (tx[1][i]["unspent"]):
                    all_unspent.append(tx)
                    break
        return all_unspent

    def findSenderUnspent(self, s_address):
        all_unspent = []
        balance = 0.0
        with open(utxo_json) as file:
            data = json.load(file)
        for tx in data:
            for i in range(len(tx[1])):
                if (tx[1][i]["unspent"] and tx[1][i]["receiver address"]==s_address):
                    all_unspent.append(tx)
                    balance += tx[1][i]["amount"]
        return all_unspent, balance

    def spendTx(self, s_address, amount):
        using_input = []
        #NOT FINISHED: should handle cases that only the sum of multiple outputs is enoguh for paying the amount
        '''
        temp_input = []
        '''
        #sum of inputs amount
        sum_of_amounts = 0.0
        #retrieve prev tx id
        index = []
        #to update the json file, store the records with amended "unspent" parameter
        new_tx = []
        continue_para = True
        
        with open(utxo_json) as file:
            data = json.load(file)
        for tx in data:
            for i in range(len(tx[1])):
                if continue_para:
                    if (tx[1][i]["unspent"] and tx[1][i]["receiver address"]==s_address):
                        if (tx[1][i]["amount"] >= amount):
                            using_input.append(tx)
                            index.append(i)
                            continue_para = False
                        sum_of_amounts += tx[1][i]["amount"]

                        #NOT FINISHED: should handle cases that only the sum of multiple outputs is enoguh for paying the amount
                        '''
                        temp_input.append(tx)
                        index.append(i)
                        if (sum_of_amounts >= amount):
                            continue_para = False
                        '''
                        #Mark the output(s) that is/are going to spend as spent
                        tx[1][i].update({"unspent":False})
            new_tx.append(tx)
            
        #update json file with amended "unspent" parameter
        with open(utxo_json, 'w') as json_file:
            json.dump(new_tx, json_file,indent=4,separators=(',',': '))
            
        return index, using_input, sum_of_amounts

    def printRecords(self):
        with open(utxo_json) as file:
            data = json.load(file)
        print("")
        print("")
        print("Current transactions in memory pool:")
        print("")
        j = 1
        for tx in data:
            print("-----transaction "+str(j)+"-----")
            print("Transaction id:"+tx[2][0])
            #print inputs
            for i in range(len(tx[0])):
                print("Previous TX id:"+tx[0][i]["previous tx id"])
                print("Previous TX index:"+str(tx[0][i]["previous tx index"]))
            #print outputs
            for i in range(len(tx[1])):
                print("Receiver address:"+tx[1][i]["receiver address"])
                print("Amount:"+str(tx[1][i]["amount"]))
                print("Unspent:"+str(tx[1][i]["unspent"]))
            print("")
            j+=1
        print("")
        print("")
