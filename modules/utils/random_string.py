import random


def create_random_string(val, len):
    result = ''

    for _ in range(len):
        result += random.choice(val)

    return result
