import string
import random
from const import const
from modules.msg_print import *
from modules.error_check import *


def execute_random_string():
    length = 16

    allows_number = True
    allows_lower = True
    allows_upper = True
    allows_punctuation = True

    number_state = "O"
    lower_state = "O"
    upper_state = "O"
    punctuation_state = "O"

    while True:
        menu = select_menu(length, number_state, lower_state,
                           upper_state, punctuation_state)
        match menu:
            case "1":
                length = int(
                    input(f"{const['REQUIRE_VALUE_LENGTH']} : "))
                clear_screen()
            case "2":
                allows_number, number_state = toggle_condition(
                    allows_number, number_state)
            case "3":
                allows_lower, lower_state = toggle_condition(
                    allows_lower, lower_state)
            case "4":
                allows_upper, upper_state = toggle_condition(
                    allows_upper, upper_state)
            case "5":
                allows_punctuation, punctuation_state = toggle_condition(
                    allows_punctuation, punctuation_state)
            case "9":
                result_panel(create_value(length, allows_number,
                                          allows_lower, allows_upper, allows_punctuation))
            case "0":
                break
            case _:
                err_panel(const['ERROR_WRONG_MENU'])


def select_menu(length, number_state, lower_state, upper_state, punctuation_state):
    display_string_menu(length, number_state, lower_state,
                        upper_state, punctuation_state)

    menu = input(const['REQUIRE_MENU'])

    return menu


def toggle_condition(flg, state):
    clear_screen()
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
