from random import randint


def create_tel_number():
    area_code = randint(10, 999)
    first_part = randint(100, 999)
    second_part = randint(1000, 9999)
    return f"{area_code}-{first_part}-{second_part}"
