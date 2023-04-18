import hashlib
import time
from datetime import datetime

def compute_sha256_as_hex_string(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()

def convert_to_hex(data):
    return data.hex()

def main():
    print("Enter some data for a small hash generation")
    print("For BabyHash, all input data is converted to lower case")
    t_begin = time.time()
    
    input_string = input().lower()
    baby_hash = "FFFF"
    i = 0

    # Your loop here

    # While the babyhash is not zero
    # {
    #     Concatenate inputString to i with the concat() function
    #     Compute the hash with ComputeSHA_256_as_Hex_String()
    #     Separates the first x characters of the hash with the substring()
    #     Display the nonce
    #     Display the hash
    #     Increment the nonce
    # }

    # End of your loop

    t_end = time.time()
    ex_time = t_end - t_begin
    print("Mining time =", ex_time, "sec")

if __name__ == "__main__":
    main()
