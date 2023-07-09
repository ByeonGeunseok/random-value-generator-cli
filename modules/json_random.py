from pathlib import Path
from json import *
import time
from conf import conf
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


def set_json_key():
    error_flg = False
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

        if error_flg:
            err_panel("There are no keys.")
            error_flg = False
        key_str = input(">> ")

        if key_str == " ":
            # Delete last key
            if len(keys) <= 0:
                error_flg = True
            else:
                keys.pop()
        elif key_str == "":
            if len(keys) <= 0:
                error_flg = True
            else:
                break
        else:
            keys.append(key_str)
        clear_screen()
    set_key_type(keys)


def set_key_type(keys):
    value_type_list = []
    data_length = len(keys)
    for _ in range(data_length):
        value_type_list.append("")

    while True:
        value_type_list = display_json_type(keys, value_type_list)
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

        match select_type:
            case "list":
                value_type_list[index] = select_type
            case "name":
                value_type_list[index] = select_type
            case "number" | "num":
                value_type_list[index] = select_type
            case "tel":
                value_type_list[index] = select_type
            case "email":
                value_type_list[index] = select_type
            case "percentage" | "per":
                value_type_list[index] = select_type
            case "boolean" | "bool":
                value_type_list[index] = select_type
            case _:
                err_panel("SELECT CORRECT MENU")
    create_json_data(keys, value_type_list)


def create_json_data(keys, value_type_list):
    json_data = {}
    index = 0
    for key in keys:
        data = ""
        match value_type_list[index]:
            case "list":
                print()
            case "name":
                data = create_random_name("full")
            case "number" | "num":
                data = create_random_number()
            case "tel":
                data = create_tel_number()
            case "email":
                data = create_email_address()
            case "percentage" | "per":
                data = str(random.randint(0, 100)) + "%"
            case "boolean" | "bool":
                data = bool(random.getrandbits(1))
            case _:
                print()
        index += 1

        json_data[key] = data
    create_json_file(json_data)


def create_json_file(json_data):
    current_time = time.strftime('%Y%m%d%H%M%S')
    path = conf['OUTPUT_PATH']
    file_name = path + "random_" + current_time + ".json"

    Path(path).mkdir(exist_ok=True)

    with open(file_name, 'w') as f:
        dump(json_data, f)
