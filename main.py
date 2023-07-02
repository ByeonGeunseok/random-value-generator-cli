from modules.number_repeat import *
from modules.number_shuffle import *
from modules.string_random import *
from modules.csv_random import *
from modules.json_random import *
from modules.error_check import *
from modules.msg_print import *
from const import const

while 1:
    is_possible = True

    # START
    render_main_menu()

    menu = input(const['REQUIRE_MENU'])

    if menu.isdigit():
        # Choose the menu
        match menu:
            # Repeat Menu
            case "1":
                execute_number_repeat()
            # Shuffle menu
            case "2":
                execute_number_shuffle()
            # Random string menu
            case "3":
                while True:
                    menu = select_menu(length, number_state, lower_state,
                                       upper_state, punctuation_state)
                    if menu == "1":
                        length = int(
                            input(f"{const['REQUIRE_VALUE_LENGTH']} : "))
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
                err_panel(const['ERROR_WRONG_MENU'])
    else:
        err_panel(const['ERROR_WRONG_MENU'])
