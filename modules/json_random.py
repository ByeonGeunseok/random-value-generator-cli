from re import match
from json import *
import os
import time
from config import config
from modules.msg_print import *
from modules.random_names import *
from modules.random_numbers import *
from modules.random_tel_nums import *
from modules.random_email import *

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
        if menu == "":
            break
        elif menu.isdigit():
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
        else:
            err_panel("SELECT CORRECT MENU")
    generate_json_data(keys, value_type_list)


def generate_json_data(keys, value_type_list):
    json_data = {}
    index = 0
    for key in keys:
        data = ""
        if value_type_list[index] == "list":
            print()
        elif value_type_list[index] == "name":
            data = create_random_name("full")
        elif value_type_list[index] == "number" or value_type_list[index] == "num":
            data = create_random_number()
        elif value_type_list[index] == "tel":
            data = create_tel_number()
        elif value_type_list[index] == "email":
            data = create_email_address()
        elif value_type_list[index] == "percentage" or value_type_list[index] == "per":
            data = str(random.randint(0, 100)) + "%"
        elif value_type_list[index] == "boolean" or value_type_list[index] == "bool":
            data = bool(random.getrandbits(1))
        else:
            print()
        index += 1

        json_data[key] = data
    create_json_file(json_data)


def create_json_file(json_data):
    current_time = time.strftime('%Y%m%d%H%M%S')
    path = "./output/"
    file_name = path + "random_" + current_time + ".json"

    if os.path.isdir("./output") == False:
        os.mkdir("./output")
        file = open(file_name, 'w', newline='')

    with open(file_name, 'w') as f:
        dump(json_data, f)
