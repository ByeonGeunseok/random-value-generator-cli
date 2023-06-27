from modules.number_repeat import *
from modules.number_shuffle import *
from modules.string_random import *
from modules.csv_random import *
from modules.json_random import *
from modules.error_check import *
from modules.msg_print import *


while 1:
    is_possible = True

    # START
    msg_main_menu()

    menu = input("Choose the menu.")

    if menu.isdigit():
        # Choose the menu
        match menu:
            # Repeat Menu
            case "1":
                amount_input = input("How many numbers do you need? : ")
                min_range_input = input("Choose a minimum range. : ")
                max_range_input = input("Choose a maximum range. : ")
                repeat_count_input = input("How many times repeat? : ")

                # If all inputs are numeric
                if check_is_number(amount_input, min_range_input, max_range_input, repeat_count_input):
                    if check_min_max(int(min_range_input), int(max_range_input)):
                        number_repeat(int(amount_input), int(min_range_input), int(
                            max_range_input), int(repeat_count_input))
                else:
                    err_panel("Please check your inputs.")
            # Shuffle menu
            case "2":
                amount_input = input("How many numbers do you need? : ")
                min_range_input = input("Choose a minimum range. : ")
                max_range_input = input("Choose a maximum range. : ")
                shuffle_count_input = input("How many times shuffle? : ")

                # If all inputs are numeric
                if check_is_number(amount_input, min_range_input, max_range_input, shuffle_count_input):
                    if check_min_max(int(min_range_input), int(max_range_input)):
                        number_shuffle(int(amount_input), int(min_range_input), int(
                            max_range_input), int(shuffle_count_input))
                else:
                    err_panel("Please check your inputs.")
            # Random string menu
            case "3":
                while True:
                    menu = select_menu(length, number_state, lower_state,
                                       upper_state, punctuation_state)
                    if menu == "1":
                        length = int(input("How long value do you need? : "))
                    elif menu == "2":
                        allows_number, number_state = toggle_condition(
                            allows_number, number_state)
                    elif menu == "3":
                        allows_lower, lower_state = toggle_condition(
                            allows_lower, lower_state)
                    elif menu == "4":
                        allows_upper, upper_state = toggle_condition(
                            allows_upper, upper_state)
                    elif menu == "5":
                        allows_punctuation, punctuation_state = toggle_condition(
                            allows_punctuation, punctuation_state)
                    elif menu == "9":
                        result_panel(create_value(length, allows_number,
                                                  allows_lower, allows_upper, allows_punctuation))
                    else:
                        break
            # Random CSV menu
            case "4":
                set_config_header()
            # Random JSON menu
            case "5":
                set_config_key()
            case "9":
                break
            case _:
                err_panel("Choose the correct menu.")
    else:
        err_panel("Choose the correct menu.")
