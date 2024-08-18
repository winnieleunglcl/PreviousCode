from utxo import Utxo
from wallet import Wallets
from ecdsaKey import getBackPrivateKeyObject, signWithPrivateKey
import numpy as np

class Input():
    def __init__(self):
        #Can have multiple inputs, so it is a list
        self.inputs = []
        self.utxo = Utxo()

    def setInput(self, s_address, amount):
        #first find sender's all unspent outputs -> utxo.py
        s_unspent, s_balance = self.utxo.findSenderUnspent(s_address)
        #Mark the output(s) that is/are going to spend as spent, and retrieve info. for next steps -> utxo.py
        index, using_input, input_amount = self.utxo.spendTx(s_address, amount)

        i=0
        for tx in s_unspent:
            each_tx_input = {
                #each transaction: [[inputs][outputs][transaction id]]
                "previous tx id":tx[2][0],
                "previous tx index":index[i],
            }
            #signature will be appended later as the process to generate transaction id doesn't include it -> transaction.py
            self.appendInput(each_tx_input)
            i+=1

        return input_amount

    def appendInput(self, tx_input):
        #append the input into the list of inputs
        self.inputs.append(tx_input)

    def appendSign(self, s_address):
        s_private_key_string = Wallets().getPrivateKey(s_address)
        s_private_key_object = getBackPrivateKeyObject(s_private_key_string)
        for tx_input in self.inputs:
            if(type(tx_input) == dict):
                tx_input_bytes = np.array(tx_input,dtype=object).tobytes()
                sign = signWithPrivateKey(s_private_key_object, tx_input_bytes)
                tx_input.update({"signature":str(sign)})
        return self.inputs
