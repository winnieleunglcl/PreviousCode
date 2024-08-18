class Output():
    def __init__(self):
        self.outputs = []

    def setOutput(self, r_address, amount):
        each_tx_output = {
            "receiver address": r_address,
            "amount": amount,
            "unspent": True
        }
        return each_tx_output

    def appendOutput(self, tx_output):
        self.outputs.append(tx_output)
