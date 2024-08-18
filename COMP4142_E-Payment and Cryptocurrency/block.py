import time
from proof_of_work import Nonce
from merkle_tree import MerkleRoot
from transaction import coinbase_transaction
from utxo import Utxo

MAX_NONCE = 2**32

class Block:
    def __init__(self):
        #each block is a dict object
        self.block = dict()

    def set_block(self, index:int, prevHash, difficulty:int, data):
        #initialize block content
        #difficulty was adjusted -> interface.py
        #data: list of transactions -> each transaction: [[inputs][outputs][transaction id]]
        block = {
            "index":index,
            "timestamp":time.time(),
            "prevHash":prevHash,
            "difficulty":difficulty,
            "nonce":0,
            "data":data
        }

        #-> merkle_tree.py
        block["root"] = MerkleRoot(data).hash

        #POW
        POW_success = False
        block["nonce"], block["currHash"], POW_success = Nonce(block, MAX_NONCE)

        #If POW succeeds, the block is valid. Else, the block is invalid and set to be an empty dict: {}
        if (POW_success):
            self.block = block
        else:
            self.block = {}
        return block

def genesis_block(difficulty, miner_of_genesis_block):
    g_block = Block().set_block(0, None, difficulty, "")
    #genesis block content is hardcoded
    g_block["data"] = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."
    #set genesis block has 50 coins rewards -> to the miner of genesis block like Satoshi Nakamoto
    #e.g., if Alice is the first person to login to this system and initialize the blockchain, she will be rewarded for 50 coins
    coinbase_transaction(Utxo(), miner_of_genesis_block, 50)
    return g_block
