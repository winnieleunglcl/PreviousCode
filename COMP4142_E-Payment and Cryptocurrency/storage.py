import json, io, os
from tool import UnixToDatetime

blockchain_json = "blockchain.json"
READPATH = "./"+blockchain_json
CURRENTPATH = "./"

class Json:
    def __init__(self):
        self.json = self.checkExistAndRead()
            
    def checkExistAndRead(self):
        if os.path.isfile(READPATH) and os.access(READPATH, os.R_OK):
            print ("Accessed blockchain!")
            with open(blockchain_json) as file:
                data = json.load(file)
            return data
        else:
            print ("No blockchain exists, creating...")
            print ("Accessed blockchain!")
            with io.open(os.path.join(CURRENTPATH, blockchain_json), 'w') as db_file:
                db_file.write(json.dumps([]))
            with open(blockchain_json) as file:
                data = json.load(file)            
            return data

    def notExist(self, block):
        block_hash = block["currHash"]
        notExist = True
        with open(blockchain_json) as file:
                data = json.load(file)
        for b in data:
            if (b["currHash"] == block_hash):
                notExist = False
        return notExist
        
    def getLastBlock(self):
        with open(blockchain_json) as file:
                data = json.load(file)
        last_block = None
        if len(data)!=0:
            last_block = data[-1]
        return last_block

    def get_tenth_blocks_before(self):
        #to get the 10th-blocks before the current block
        with open(blockchain_json) as file:
            data = json.load(file)
        return data[-10]

    def append(self, block):
        with open(blockchain_json) as file:
                data = json.load(file)
        data.append(block)
        with open(blockchain_json, 'w') as json_file:
            json.dump(data, json_file,indent=4,separators=(',',': '))

    def printBlocks(self):
        with open(blockchain_json) as file:
                data = json.load(file)
        print("")
        for i in range(len(data)):
            block = data[i]
            print("-----block "+str(i)+"-----")
            print("index: "+str(block["index"]))
            print("timestamp: "+str(UnixToDatetime(int(block["timestamp"]))))
            print("previous block hash: "+str(block["prevHash"]))
            print("current block hash: "+str(block["currHash"]))
            print("difficulty: "+str(block["difficulty"]))
            print("nonce: "+str(block["nonce"]))
            print("merkle root of transactions: "+str(block["root"]))
            print("data: "+str(block["data"]))
            print("")
