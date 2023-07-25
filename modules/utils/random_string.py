from random import choice


def create_random_string(val, len):
    result = ''

    for _ in range(len):
        result += choice(val)

    return result
