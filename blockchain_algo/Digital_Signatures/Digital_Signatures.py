from ecdsa import SigningKey, SECP256k1


def generate_keys():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key


def sign_data(private_key, data):
    return private_key.sign(data.encode())


def verify_signature(public_key, signature, data):
    return public_key.verify(signature, data.encode())


private_key, public_key = generate_keys()
data = "Transaction data"
signature = sign_data(private_key, data)

print(f"Data: {data}")
print(f"Signature: {signature}")
print(f"Verification: {verify_signature(public_key, signature, data)}")
