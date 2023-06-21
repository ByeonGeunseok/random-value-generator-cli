from modules.number_repeat import number_repeat
from modules.number_shuffle import number_shuffle
from modules.error_check import check_min_max

while 1:
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
            case 1:
                amount_input = int(input("How many numbers do you need? : "))
                min_range_input = int(input("Choose a minimum range. : "))
                max_range_input = int(input("Choose a maximum range. : "))
                repeat_count_input = int(input("How many times repeat? : "))

                if check_min_max(min_range_input, max_range_input):
                    number_repeat(amount_input, min_range_input,
                                  max_range_input, repeat_count_input)
            case 2:
                amount_input = int(input("How many numbers do you need? : "))
                min_range_input = int(input("Choose a minimum range. : "))
                max_range_input = int(input("Choose a maximum range. : "))
                shuffle_count_input = int(input("How many times shuffle? : "))

                if check_min_max(min_range_input, max_range_input):
                    number_shuffle(amount_input, min_range_input,
                                   max_range_input, shuffle_count_input)
            case 9:
                break
            case _:
                print("Choose the correct menu.")
    else:
        print("Choose the correct menu.")
