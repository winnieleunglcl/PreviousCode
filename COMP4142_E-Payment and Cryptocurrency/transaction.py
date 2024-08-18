from output import Output
from input import Input
from wallet import Wallets
import numpy as np
from tool import Sha256
#from p2pkh import p2pkh

class Transaction():
    def __init__(self):
        self.transaction = []
        self.inputClass = Input()
        self.outputClass = Output()
        self.wallets = Wallets()
        self.valid = True

    def set_transaction(self, s_address, r_address, amount):
        tx_output = self.outputClass.setOutput(r_address, amount)
        #If not coinbase transaction,
        if s_address != None:
            #Input:
            sender_balance = self.wallets.getBalance(s_address)
            #If enough balance and receiver address valid,
            if sender_balance >= amount and self.wallets.checkReceiverExist(r_address) and s_address!=r_address:
                input_amount = self.inputClass.setInput(s_address, amount)
                #Output:
                #if coins are not used up, return the remaining amount to sender = one more output with remaining amount to sender
                if (input_amount > amount):
                    self.outputClass.appendOutput(tx_output)
                    return_output = self.outputClass.setOutput(s_address, input_amount-amount)
                    self.outputClass.appendOutput(return_output)
                else:
                    self.outputClass.appendOutput(tx_output)
            else:
                print("not enough balance in wallet or receiver address invalid.")
                self.valid = False
        else:
            #if coinbase transaction
            self.outputClass.appendOutput(tx_output)
            print("Gained block reward.")
        return self.inputClass.inputs, self.outputClass.outputs

    def combine_transaction(self, inputs, outputs):
        #make transaction structure: [[inputs with sign][outputs]]
        self.transaction.append(inputs)
        self.transaction.append(outputs)

    def temp_combine_transaction(self, inputs, outputs):
        #make transaction structure: [[inputs without sign][outputs]]
        temp_tx = []
        temp_tx.append(inputs)
        temp_tx.append(outputs)
        return temp_tx

    def add_transaction(self, utxo_file, s_address, r_address, amount):
        inputs, outputs = self.set_transaction(s_address, r_address, amount)
        #get a temporary transaction structure without signature for generating transaction id
        temp_tx = self.temp_combine_transaction(inputs, outputs)

        #add back signature to each input
        if (s_address!=None):
            new_inputs = self.inputClass.appendSign(s_address)

        #transaction:[[inputs][outputs]]
        self.combine_transaction(inputs, outputs)

        #turn inputs and outputs to bytes, then hash it to become transaction id
        transaction_bytes = np.array(temp_tx,dtype=object).tobytes()
        transaction_id = Sha256(transaction_bytes)
        self.transaction.append([transaction_id])

        #p2pkh verification: NOT FINISHED -> pls refer to p2pkh.py

        #transaction:[[inputs][outputs][transaction id]]
        if (self.valid):
            print("Success transaction.")
            utxo_file.appendUtxoRecord(self.transaction)
            self.wallets.updateBalance()

def coinbase_transaction(utxo_file, r_address, amount):
    c_tx = Transaction()
    c_tx.add_transaction(utxo_file, None, r_address, amount)
    return c_tx.transaction
