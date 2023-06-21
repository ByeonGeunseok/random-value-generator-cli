from modules.number_repeat import number_repeat
from modules.number_shuffle import number_shuffle
from modules.error_check import *

while 1:
    is_possible = True

    # START
    print("-*- -*- -*- -*- -*- -*- -*-")
    print("CHOOSE THE MENU")
    print("1 -> repeat")
    print("2 -> shuffle")
    print("9 -> Exit from this app.")
    print("-*- -*- -*- -*- -*- -*- -*-")

    menu = input("Choose the menu.")

    if menu.isdigit():
        # Choose the menu
        match int(menu):
            # Repeat Menu
            case 1:
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
                    print("Please check your inputs.")
            # Shuffle menu
            case 2:
                amount_input = input("How many numbers do you need? : ")
                min_range_input = input("Choose a minimum range. : ")
                max_range_input = input("Choose a maximum range. : ")
                shuffle_count_input = input("How many times shuffle? : ")

                # If all inputs are numeric
                if check_is_number(amount_input, min_range_input, max_range_input, shuffle_count_input):
                    if check_min_max(int(min_range_input), int(max_range_input)):
                        number_repeat(int(amount_input), int(min_range_input), int(
                            max_range_input), int(shuffle_count_input))
                else:
                    print("Please check your inputs.")

            case 9:
                break
            case _:
                print("Choose the correct menu.")
    else:
        print("Choose the correct menu.")
