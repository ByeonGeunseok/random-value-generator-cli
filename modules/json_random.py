from re import match
from modules.msg_print import *

global keys
global value_type_list
global json_data
keys = []
value_type_list = []
json_data = {}


def set_config_key():
    while True:
        msg = "Input a key.\n" + \
            "If you delete to last key, input \" \" and ENTER.\n" + \
            "If you done to input key, Just press ENTER."
        title = "Random JSON"
        msg_panel(msg, title)

        if len(keys) <= 0:
            msg_panel("key: (nothing)", "KEY")
        else:
            msg_panel(f"key: {keys}", "KEY")
        key_str = input(">> ")

        if key_str == " ":
            # Delete last key
            if len(keys) <= 0:
                err_panel("There are no keys.")
            else:
                keys.pop()
        elif key_str == "":
            if len(keys) <= 0:
                err_panel("There are no keys.")
            else:
                break
        else:
            keys.append(key_str)

    set_key_type(keys)


def set_key_type(keys):
    value_type_list = []
    data_length = len(keys)
    for _ in range(data_length):
        value_type_list.append("")

    while True:
        value_type_list = msg_json_type(keys, value_type_list)
        menu = input("Choose the menu >> ")
        if menu.isdigit():
            if int(menu) <= data_length and menu != "0":
                index = int(menu) - 1
            else:
                err_panel("CHOOSE CORRECT MENU")
                continue
        else:
            err_panel("CHOOSE CORRECT MENU")
            continue

        msg_panel(
            f"((name/number/num/tel/email/percentage/per/boolean/bool))", "TYPE SELECT")
        select_type = input(">> ")

        if select_type == "list":
            value_type_list[index] = select_type
        elif select_type == "name":
            value_type_list[index] = select_type
        elif select_type == "number" or "num":
            value_type_list[index] = select_type
        elif select_type == "tel":
            value_type_list[index] = select_type
        elif select_type == "email":
            value_type_list[index] = select_type
        elif select_type == "percentage" or "per":
            value_type_list[index] = select_type
        elif select_type == "boolean" or "bool":
            value_type_list[index] = select_type
        elif select_type == "":
            print("TODO: NEXT STEP")
        else:
            err_panel("SELECT CORRECT MENU")


def set_config_value(keys, type_list):
    index = 0
    for type in type_list:
        if type == "DATA":
            msg_panel(f"Input value of {keys[index]}", "VALUE")
            value = input(">> ")

            if is_number_or_decimal(value):
                msg_panel("Is it number?", "")
                answer_number = input("(y/n) >> ")

                if answer_number == "y":
                    if "." in value:
                        value = float(value)
                    else:
                        value = int(value)

            elif is_boolean(value):
                msg_panel("Is it boolean?", "")
                answer_bool = input("(y/n) >> ")

                if answer_bool == "y":
                    if value.lower() == "true":
                        value = bool("boolean")
                    else:
                        value = bool("")

            json_data[keys[index]] = value
        else:
            # list def
            print()
        index += 1
    print(json_data)


def is_number_or_decimal(string) -> bool:
    number_pattern = r'^-?\d+\.?\d*$'
    decimal_pattern = r'^-?\d+\.\d+$'

    if match(number_pattern, string):
        return True
    elif match(decimal_pattern, string):
        return True
    else:
        False


def is_boolean(string) -> bool:
    if string.lower() == "true":
        return True
    elif string.lower() == "false":
        return True
    else:
        return False
