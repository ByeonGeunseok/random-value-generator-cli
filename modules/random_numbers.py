import random

def create_random_number():
    random_number_string = ""
    for _ in range(random.randint(4, 9)):
        random_number_string += str(random.randint(1, 9))

    return random_number_string