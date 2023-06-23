import string
import random

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
    print("")
    print("-*- -*- -*- -*- -*- -*- -*-")
    print("-*- -*- -*- -*- -*- -*- -*-")
    print("[1] LENGTH : ", length)
    print("-*- -*- -*- -*- -*- -*- -*-")
    print("[2] Number : ", number_state)
    print("[3] Lower case : ", lower_state)
    print("[4] Upper case : ", upper_state)
    print("[5] Punctuation : ", punctuation_state)
    print("[9] Execute")
    print("[0] Done")
    print("-*- -*- -*- -*- -*- -*- -*-")
    print("-*- -*- -*- -*- -*- -*- -*-")

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


while True:
    menu = select_menu(length, number_state, lower_state,
                       upper_state, punctuation_state)
    if menu == "1":
        length = int(input("How long value do you need? : "))
    elif menu == "2":
        allows_number, number_state = toggle_condition(
            allows_number, number_state)
    elif menu == "3":
        allows_lower, lower_state = toggle_condition(allows_lower, lower_state)
    elif menu == "4":
        allows_upper, upper_state = toggle_condition(allows_upper, upper_state)
    elif menu == "5":
        allows_punctuation, punctuation_state = toggle_condition(
            allows_punctuation, punctuation_state)
    elif menu == "9":
        print(create_value(length, allows_number,
              allows_lower, allows_upper, allows_punctuation))
    else:
        break
