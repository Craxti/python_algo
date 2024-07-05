import random
import hashlib


class Validator:
    def __init__(self, address, stake):
        self.address = address
        self.stake = stake


class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.index}{self.previous_hash}{self.data}".encode())
        return sha.hexdigest()


class BlockchainPoS:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = []

    @staticmethod
    def create_genesis_block():
        return Block(0, "0", "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(last_block.index + 1, last_block.hash, data)
        self.chain.append(new_block)

    def add_validator(self, validator):
        self.validators.append(validator)


class DPoSValidator(Validator):
    def __init__(self, address, stake, delegated_stake=0):
        super().__init__(address, stake)
        self.delegated_stake = delegated_stake


class BlockchainDPoS(BlockchainPoS):
    def select_validator(self):
        total_stake = sum(v.stake + v.delegated_stake for v in self.validators)
        pick = random.uniform(0, total_stake)
        current = 0
        for validator in self.validators:
            current += validator.stake + validator.delegated_stake
            if current > pick:
                return validator


blockchain = BlockchainDPoS()
blockchain.add_validator(DPoSValidator("Validator1", 50, 20))
blockchain.add_validator(DPoSValidator("Validator2", 30, 10))
blockchain.add_validator(DPoSValidator("Validator3", 20, 15))

blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")

for block in blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}")
