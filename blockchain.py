import hashlib

class MyBlockChain:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions

        self.blockData = "-".join(transactions) + "-" + previous_hash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

transaction1 = "John sends 5 BC to Alan"
transaction2 = "Alan sends 6.2 BC to Dan"
transaction3 = "Mark sends 12 BC to John"
transaction4 = "Dan sends 3 BC to Ann"
transaction5 = "Ann sends 1.5 BC to Mark"

first_block = MyBlockChain("First Block", [transaction1, transaction2])

print(first_block.blockData)
print(first_block.blockHash)

second_block = MyBlockChain(first_block.blockHash, [transaction3, transaction4])

print(second_block.blockData)
print(second_block.blockHash)

