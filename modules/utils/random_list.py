import string
import random
from .random_names import create_random_name
from .random_numbers import create_random_number
from .random_email import create_email_address
from .random_tel_nums import create_tel_number
from .random_string import create_random_string


def create_random_list(type, cnt):
    li = []

    match type:
        case 'str':
            for _ in range(int(cnt)):
                val = ''
                letter = string.ascii_letters
                val = create_random_string(letter, 4)
                li.append(val)
        case 'number':
            for _ in range(int(cnt)):
                li.append(create_random_number())
        case 'name':
            for _ in range(int(cnt)):
                li.append(create_random_name('full'))
        case 'email':
            for _ in range(int(cnt)):
                li.append(create_email_address())
        case 'tel':
            for _ in range(int(cnt)):
                li.append(create_tel_number())
        case _:
            for _ in range(int(cnt)):
                li.append('')
    return li
