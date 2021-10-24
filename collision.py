from sha256 import sha256

import string
import random


def generate_random_str(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def find_collision():
    previous_keys = set()
    successful_hashes = 0

    while True:
        random_key = generate_random_str()

        print(f'random_key = {random_key}')

        hashed_key = sha256(random_key)

        if hashed_key not in previous_keys:
            previous_keys.add(hashed_key)
            successful_hashes += 1
        else:
            break

    print(f'tries: {successful_hashes} before collision')


find_collision()
