#This file is not used. Due to time limit, not combine p2pkh part with transaction yet
#P2PKH process is learnt from: https://learnmeabitcoin.com/technical/p2pkh // https://learnmeabitcoin.com/technical/p2pk
import hashlib
from eccdsaKey import verifyWithPublicKey

class p2pkh:
    def __init__(self, sender_public_key, sender_signature, sender_public_key_by_receiver, message):
        #use list to be stack, append() to push, pop() to pop
        self.stack = []
        self.sender_public_key = sender_public_key
        self.sender_signature = sender_signature
        self.sender_public_key_by_receiver = sender_public_key_by_receiver
        self.message = message
        #response script
        self.scriptSig()
        #challenge script 
        self.result = self.scriptPubKey()

    def scriptSig(self):
        #first, push sender's public key and signature to the stack for later verification
        self.stack.append(self.sender_signature)
        print(self.stack)

    def scriptPubKey(self):
        success = False
        self.OP_DUP()
        print(self.stack)
        self.OP_HASH160()
        print(self.stack)
        if self.OP_EQUALVERIFY():
            print(self.stack)
            if self.OP_CHECKSIG():
                success = True
        return success

    def OP_DUP(self):
        self.stack.append(self.sender_public_key)

    def OP_HASH160(self):
        dup_public_key_from_scriptSig = self.stack.pop()
        hash160_dup_public_key_from_scriptSig = ripemd160(dup_public_key_from_scriptSig)
        self.stack.append(hash160_dup_public_key_from_scriptSig)

    def OP_EQUALVERIFY(self):
        hash160_public_key_from_scriptSig = self.stack.pop()
        hash160_public_key_from_scriptPubKey = ripemd160(self.sender_public_key_by_receiver)
        return hash160_public_key_from_scriptSig == hash160_public_key_from_scriptPubKey

    def OP_CHECKSIG(self):
        sign_from_scriptSig = self.sender_signature
        success = verifyWithPublicKey(sender_public_key_by_receiver, sign_from_scriptSig, self.message)
        return success
        
def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d

