import hashlib
from datetime import datetime
import time

MAX_NONCE = 2**32

def Sha256(msg):
    sha256 = hashlib.sha256()
    sha256.update(msg)
    return sha256.hexdigest()

def ValidateBlock(new_block, prev_block):
    valid = True
    if (prev_block != None):
        #index of current block must be exactly 1 larger than that of the previous block
        if (new_block["index"]-prev_block["index"] != 1):
            valid = False
            print("Invalid index")
        #prevHash of current block must equal to the hash field of previous block
        if (new_block["prevHash"] != prev_block["currHash"]):
            valid = False
            print("Invalid prevHash")
        #timestamp field of current block is supposed to be after that of the previous block and before current time
        if (new_block["timestamp"] < prev_block["timestamp"] and new_block["timestamp"] > time.time()):
            valid = False
            print("Invalid timestamp")

        #nonce & hash of current block itself must be valid -> checked by POW
        #difficulty field of current block must be calculated according to the block-out rate -> blockchain.py:adjust_difficulty()
        #transactions in data field of current block must be valid -> each transaction should be valid before adding to memory pool

    return valid

def UnixToDatetime(time:float):
    #Epoch time to date time
    return datetime.fromtimestamp(time)

def HexToBin(hexstr: str) -> str:
    template = "{:0" + str(len(hexstr)*4) + "b}" 
    return template.format((int(hexstr, 16)))
