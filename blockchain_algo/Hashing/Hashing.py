import hashlib


def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()


data = "Hello, Blockchain!"
hash_result = sha256(data)
print(f"Data: {data}, SHA-256 Hash: {hash_result}")
