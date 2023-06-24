import random


def generate_fake_phone_number():
    area_code = random.randint(10, 999)
    first_part = random.randint(100, 999)
    second_part = random.randint(1000, 9999)
    return f"{area_code}-{first_part}-{second_part}"
