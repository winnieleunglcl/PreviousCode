from block import genesis_block
from storage import Json
from tool import ValidateBlock

class Blockchain:
    def __init__(self, miner_of_genesis_block):
        #store the blockchain in json -> storage.py
        self.blockchain = Json()
        #initialize genesis block if new blockchain, difficulty = 1
        if self.blockchain.getLastBlock() == None:
            first_block = genesis_block(1, miner_of_genesis_block)
            self.blockchain.append(first_block)

    def add_block_to_chain(self, new_block):
        #check if pow passed
        if (new_block != {}):
            print("POW passed.")
            #validate block before adding
            if ValidateBlock(new_block, self.blockchain.getLastBlock()):
                print("Validation of block passed.")
                #check if the block exists
                if self.blockchain.notExist(new_block):
                    self.blockchain.append(new_block)
                    print('Successfully appended to the blockchain!')
            else:
                print("Validation of block failed.")
        else:
            print("POW failed.")
                    
    def get_height(self):
        return self.blockchain.getLastBlock()["index"]
    
    def print_blockchain(self):
        self.blockchain.printBlocks()

    def get_current_difficulty(self):
        return self.blockchain.getLastBlock()['difficulty']

    def adjust_difficulty(self):
        
        #the difficulty of each block is changed according to previous 10th block time (last block timestamp - previous 10th block timestamp)
        #Expected time = 10 * 600 s = 6000 s
        
        if ((self.blockchain.getLastBlock()['index']+1)%10==0):
            xy=int(self.blockchain.getLastBlock()['timestamp']-self.blockchain.get_tenth_blocks_before()['timestamp'])
            #new difficulty = old difficulty * ( nTime difference / expected time )
            new_difficulty=(self.blockchain.getLastBlock()['difficulty'])*(xy/6000)
            if new_difficulty < 1:  #set difficult at least 1
                new_difficulty=1
            new_difficulty = round(new_difficulty)
        else:
            new_difficulty = self.blockchain.getLastBlock()['difficulty']
        return new_difficulty

