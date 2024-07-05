import random
import time
import hashlib


class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode())
        return sha.hexdigest()


class Validator:
    def __init__(self, address, stake):
        self.address = address
        self.stake = stake


class BlockchainPoS:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = []

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_validator(self, validator):
        self.validators.append(validator)

    def select_validator(self):
        total_stake = sum(v.stake for v in self.validators)
        pick = random.uniform(0, total_stake)
        current = 0
        for validator in self.validators:
            current += validator.stake
            if current > pick:
                return validator

    def add_block(self, data):
        validator = self.select_validator()
        new_block = Block(len(self.chain), self.get_latest_block().hash, int(time.time()), data)
        new_block.previous_hash = self.get_latest_block().hash
        self.chain.append(new_block)
        print(f"Block added by {validator.address}")


blockchain = BlockchainPoS()
blockchain.add_validator(Validator("Validator1", 50))
blockchain.add_validator(Validator("Validator2", 30))
blockchain.add_validator(Validator("Validator3", 20))

blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")

for block in blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}")
