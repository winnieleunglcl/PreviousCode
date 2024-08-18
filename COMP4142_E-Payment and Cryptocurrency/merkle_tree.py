#from COMP4142 lab 1
import hashlib
import math


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.hash = calculate_hash(self.value)


def calculate_hash(value):
    return hashlib \
        .sha256(value.encode('utf-8')) \
        .hexdigest()


def build_merkle_tree(leaves):
    nodes = []

    for i in leaves:
        nodes.append(Node(i))

    while len(nodes) != 1:
        temp = []
        for i in range(0, len(nodes), 2):
            node1 = nodes[i]
            node2 = nodes[i + 1]
            concat_hash = node1.hash + node2.hash
            parent = Node(concat_hash)
            parent.left = node1
            parent.right = node2
            temp.append(parent)
        nodes = temp
    return nodes[0]


def padding(leaves):
    size = len(leaves)
    if size == 0:
        return ['']
    reduced_size = int(math.pow(2, int(math.log2(size))))
    pad_size = 0
    if reduced_size != size:
        pad_size = 2 * reduced_size - size
    for i in range(pad_size):
        leaves.append('')
    return leaves

def MerkleRoot(transactions):
    #As the transactions is a list of transactions, not able to use this method now
    #First turn each transaction in the list into string first
    #then append each to txs
    txs = []
    for tx in transactions:
        s = ''.join(str(x) for x in tx)
        txs.append(s)
    leaves = padding(txs)
    merkle_root = build_merkle_tree(leaves)
    return merkle_root
