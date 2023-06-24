import random


def create_random_number():
    random_number_string = ""
    for _ in range(random.randint(4, 8)):
        if not random_number_string:
            random_number_string += str(random.randint(1, 9))
        else:
            random_number_string += str(random.randint(0, 9))

    return random_number_string
