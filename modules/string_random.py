import string
import random
from modules.msg_print import *

global allows_number
global allows_lower
global allows_upper
global allows_punctuation

length = 16

allows_number = True
allows_lower = True
allows_upper = True
allows_punctuation = True

number_state = "O"
lower_state = "O"
upper_state = "O"
punctuation_state = "O"


def select_menu(length, number_state, lower_state, upper_state, punctuation_state):
    msg_string_menu(length, number_state, lower_state,
                    upper_state, punctuation_state)

    menu = input("Select the menu.")

    return menu


def toggle_condition(flg, state):
    if flg:
        state = "X"
    else:
        state = "O"
    flg = not flg

    return flg, state


def create_value(length, allows_number, allows_lower, allows_upper, allows_punctuation):
    result = ""
    target = ""

    if allows_number:
        target += string.digits
    if allows_lower:
        target += string.ascii_lowercase
    if allows_upper:
        target += string.ascii_uppercase
    if allows_punctuation:
        target += string.punctuation

    for i in range(length):
        result += random.choice(target)

    return result
