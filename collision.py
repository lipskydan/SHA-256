from sha256 import sha256

import string
import random

import time


def time_exec(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__}: works {end - start}s')
    return wrapper


def generate_random_str(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@time_exec
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
