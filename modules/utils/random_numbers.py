from random import randint


def create_random_number():
    random_number_string = ""
    for _ in range(randint(4, 8)):
        if not random_number_string:
            random_number_string += str(randint(1, 9))
        else:
            random_number_string += str(randint(0, 9))

    return random_number_string
