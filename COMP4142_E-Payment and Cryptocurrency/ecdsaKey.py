#method usage refers to: https://pypi.org/project/ecdsa/
import ecdsa
from ecdsa import SigningKey, VerifyingKey
from tool import Sha256

def keyGen():
    #private key:
    sk = SigningKey.generate(curve=ecdsa.SECP256k1) #256-bit curve secp256k1 used by Bitcoin
    #public key:
    vk = sk.verifying_key

    #key object -> bytes
    sk_string = sk.to_string()
    vk_string = vk.to_string()

    #for simplicity, hash public key to get bitcoin address
    bitcoin_address = Sha256(vk_string)

    #for keys in bytes, turn them into str for json storage
    return str(sk_string), str(vk_string), bitcoin_address

def getBackPrivateKeyObject(private_key_string):
    #str -> bytes
    eval_private_key_string = eval(private_key_string)
    #bytes -> key object for signing and verifying
    private_key_object = SigningKey.from_string(eval_private_key_string,curve=ecdsa.SECP256k1)
    return private_key_object

def getBackPublicKeyObject(public_key_string):
    #str -> bytes
    eval_public_key_string = eval(public_key_string)
    #bytes -> key object for signing and verifying
    public_key_object = VerifyingKey.from_string(eval_public_key_string,curve=ecdsa.SECP256k1)
    return public_key_object

def signWithPrivateKey(private_key_object, message:bytes):
    signature = private_key_object.sign(message)
    return signature

def verifyWithPublicKey(public_key_object, signature, message:bytes):
    success = public_key_object.verify(signature, message)
    return success

#pri, pub, add = keyGen()
#pri_object, pub_object = getBackKeyObject(pri, pub)
#sign = signWithPrivateKey(pri_object, b"message")
#verify = verifyWithPublicKey(pub_object, sign, b"message")
