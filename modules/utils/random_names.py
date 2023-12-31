from random import choice
from message import message
from .msg_print import display_name_type

first_names = message['FIRST_NAME_EN']

last_names = message['LAST_NAME_EN']


def choose_name_type():
    display_name_type()
    name_type = input("Choose : ")

    match name_type:
        case "1":
            return f"name_first"
        case "2":
            return f"name_last"
        case "3":
            return f"name_full"
        case _:
            return f"name_full"


def create_random_name(name_type):
    if name_type == "first":
        return choice(first_names)
    elif name_type == "last":
        return choice(last_names)
    elif name_type == "full":
        full_name = choice(first_names) + " " + \
            choice(last_names)
        return full_name
    else:
        return 0
