#Modified COMP4142 lab 1 code
import hashlib
import json
from tool import HexToBin

# perform PoW in a iteration manner
def proof_of_work(block_content, difficulty, target, MAX_NONCE):
    # perform the iteration, until finding a nonce which satisfies the target
    for nonce in range(MAX_NONCE):
        block_content["nonce"] = nonce
        block_content_bytes = json.dumps(block_content,indent=2).encode('utf-8')
        hash_res = CalBlockHash(block_content_bytes)
        if int(hash_res, 16) < target and ValidateHash(hash_res,difficulty):
            return nonce, hash_res, True
    # target cannot be satisfied even all nonces are traversed
    print(f'failed after {MAX_NONCE} tries\n')
    return MAX_NONCE, None, False

#define block hash content for further calculation of nonce and hash
def Nonce(block, MAX_NONCE):
    target = 2**(256 - block["difficulty"])
    block_content = {
        "index":block["index"],
        "merkle_root":block["root"],
        "timestamp":block["timestamp"],
        "prevHash":block["prevHash"],
        "difficulty":block["difficulty"],
        "nonce":block["nonce"]
    }
    return proof_of_work(block_content, block_content["difficulty"], target, MAX_NONCE)

#compare number of 0 at the beginning of block hash with difficulty
def ValidateHash(blockHash, difficulty):
    hashBinary = HexToBin(blockHash)
    validHash = '0'*difficulty
    if (hashBinary[2:difficulty+2] != validHash):
        return False
    return True

#double SHA256
def CalBlockHash(data:bytes):
    h = hashlib.sha256(data).digest()
    return hashlib.sha256(h).hexdigest()
