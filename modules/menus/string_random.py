import string
import random
import clipboard
from const import const
from ..utils.msg_print import *
from ..utils.error_check import *
from ..utils.random_string import *


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

    error_type = 0

    while True:
        display_string_menu(length, number_state, lower_state,
                            upper_state, punctuation_state)

        if error_type == 1:
            err_panel(const['ERROR_INPUT'])
        elif error_type == 2:
            err_panel(const['ERROR_LENGTH_ZERO'])
        elif error_type == 3:
            err_panel(const['ERROR_ALLOWS'])
        elif error_type == 4:
            err_panel(const['ERROR_WRONG_MENU'])

        error_type = 0

        menu = input(const['REQUIRE_MENU'])

        match menu:
            case "1":
                length_val = input(f"{const['REQUIRE_VALUE_LENGTH']} : ")

                if not length_val.isdigit():
                    error_type = 1
                    continue

                if length <= 0:
                    error_type = 2
                    continue

                length = int(length_val)
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
                clear_screen()
                if number_state == "X" and lower_state == "X" and upper_state == "X" and punctuation_state == "X":
                    error_type = 3
                    continue
                else:
                    create_value(length, allows_number, allows_lower,
                                 allows_upper, allows_punctuation)
            case "0":
                break
            case _:
                error_type = 4
                clear_screen()
                continue


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

    result = create_random_string(target, length)
    clipboard.copy(result)

    result_panel(result)
    msg_panel("Copy to clipboard.", "")
    input(const['REQUIRE_CONTINUE'])
    clear_screen()
