import hashlib
import random
import string

def random_string(length=8):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def find_md5_collision():
    """Continuously generate random strings and check for MD5 hash collisions."""
    hash_dict = {}  # Store hashes and their corresponding inputs

    while True:
        # Generate a random input
        input_str = random_string(8)
        # Calculate its MD5 hash
        md5_hash = hashlib.md5(input_str.encode()).hexdigest()

        # Check if this hash already exists
        if md5_hash in hash_dict:
            print(f"Collision found!\nHash: {md5_hash}")
            print(f"String 1: {hash_dict[md5_hash]}")
            print(f"String 2: {input_str}")
            break
        else:
            # Store the hash and input in the dictionary
            hash_dict[md5_hash] = input_str

if __name__ == "__main__":
    print("Starting MD5 collision search. This may take a very long time...")
    find_md5_collision()
