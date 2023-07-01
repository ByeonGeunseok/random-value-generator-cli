from modules.number_repeat import *
from modules.number_shuffle import *
from modules.string_random import *
from modules.csv_random import *
from modules.json_random import *
from modules.error_check import *
from modules.msg_print import *
from conf import config

while 1:
    is_possible = True

    # START
    render_main_menu()

    menu = input(config['REQUIRE_MENU'])

    if menu.isdigit():
        # Choose the menu
        match menu:
            # Repeat Menu
            case "1":
                amount_input = input(f"{config['REQUIRE_NUMBER_NEED']} : ")
                min_range_input = input(f"{config['REQUIRE_MINIMUM']} : ")
                max_range_input = input(f"{config['REQUIRE_MAXIMUM']} : ")
                repeat_count_input = input(
                    f"{config['REQUIRE_REPEAT_COUNT']} : ")

                # If all inputs are numeric
                if check_is_number(amount_input, min_range_input, max_range_input, repeat_count_input):
                    if check_min_max(int(min_range_input), int(max_range_input)):
                        if check_range_cnt(int(amount_input), int(min_range_input), int(max_range_input)):
                            calc_number_repeat(int(amount_input), int(min_range_input), int(
                                max_range_input), int(repeat_count_input))
                else:
                    err_panel(config['ERROR_INPUT'])
            # Shuffle menu
            case "2":
                amount_input = input(f"{config['REQUIRE_NUMBER_NEED']} : ")
                min_range_input = input(f"{config['REQUIRE_MINIMUM']} : ")
                max_range_input = input(f"{config['REQUIRE_MAXIMUM']} : ")
                shuffle_count_input = input(
                    f"{config['REQUIRE_SHUFFLE_COUNT']} : ")

                # If all inputs are numeric
                if check_is_number(amount_input, min_range_input, max_range_input, shuffle_count_input):
                    if check_min_max(int(min_range_input), int(max_range_input)):
                        if check_range_cnt(int(amount_input), int(min_range_input), int(max_range_input)):
                            calc_number_shuffle(int(amount_input), int(min_range_input), int(
                                max_range_input), int(shuffle_count_input))
                else:
                    err_panel(config['ERROR_INPUT'])
            # Random string menu
            case "3":
                while True:
                    menu = select_menu(length, number_state, lower_state,
                                       upper_state, punctuation_state)
                    if menu == "1":
                        length = int(
                            input(f"{config['REQUIRE_VALUE_LENGTH']} : "))
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
                err_panel(config['ERROR_WRONG_MENU'])
    else:
        err_panel(config['ERROR_WRONG_MENU'])
