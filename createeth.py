import os
import hashlib
from ecdsa import SigningKey, SECP256k1

def generate_wif():
    # Generate a random 256-bit private key
    private_key = os.urandom(32)

    # Convert the private key to a WIF (Wallet Import Format) string
    wif = '0x' + private_key.hex()
    return wif

def generate_eth_address(wif):
    # Extract the private key from the WIF string
    private_key = bytes.fromhex(wif[2:])

    # Create an ECDSA signing key object
    signing_key = SigningKey.from_string(private_key, curve=SECP256k1)

    # Get the corresponding public key
    verifying_key = signing_key.get_verifying_key()

    # Compress the public key
    public_key_compressed = bytes.fromhex('04' + verifying_key.to_string().hex())

    # Hash the public key using Keccak-256
    pubkey_hash = hashlib.sha3_256(public_key_compressed).digest()

    # Take the last 20 bytes of the hash as the Ethereum address
    eth_address = '0x' + pubkey_hash[-20:].hex()

    return eth_address

# Generate a random WIF and corresponding Ethereum address
wif = generate_wif()
eth_address = generate_eth_address(wif)

print("WIF:", wif)
print("Ethereum Address:", eth_address)