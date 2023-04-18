import hashlib
from binascii import unhexlify, hexlify

def calculate_block_hash(block):
    version = block[0:8]
    hash_prev_block = block[8:72]
    hash_merkle_root = block[72:136]
    timestamp = block[136:144]
    target = block[144:152]
    nonce = block[152:160]

    header_hex = version + hash_prev_block + hash_merkle_root + timestamp + target + nonce
    header_bin = unhexlify(header_hex)
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    return hexlify(hash[::-1]).decode("utf-8")

block = "0100000081cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122bc7f5d74df2b9441a42a14695"

print("Block hash:", calculate_block_hash(block))
