from pathlib import Path
from json import *
import random
import time
from conf import conf
from const import const
from ..utils import random_list
from ..utils import msg_print
from ..utils import random_names
from ..utils import random_numbers
from ..utils import random_tel_nums
from ..utils import random_email

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
        msg_print.msg_panel(msg, title)

        if len(keys) <= 0:
            msg_print.msg_panel("key: (nothing)", "KEY")
        else:
            msg_print.msg_panel(f"key: {keys}", "KEY")

        if error_flg:
            msg_print.err_panel("There are no keys.")
            error_flg = False
        key_str = input(">> ")

        if key_str == " ":
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
        msg_print.clear_screen()
    set_key_type(keys)


# TODO: Add a object
def set_key_type(keys):
    value_type_list = []
    data_length = len(keys)
    for _ in range(data_length):
        value_type_list.append("")

    while True:
        value_type_list = msg_print.display_json_type(keys, value_type_list)
        menu = input("Choose the menu >> ")
        if menu == "":
            break
        elif menu.isdigit():
            if int(menu) <= data_length and menu != "0":
                index = int(menu) - 1
            else:
                msg_print.err_panel("CHOOSE CORRECT MENU")
                continue
        else:
            msg_print.err_panel("CHOOSE CORRECT MENU")
            continue

        msg_print.display_type_selector('json')
        select_type = input(">> ")

        match select_type:
            case "name" | "na":
                msg_print.display_name_type()
                name_menu = input(">> ")
                match name_menu:
                    case "1":
                        value_type_list[index] = "First Name"
                    case "2":
                        value_type_list[index] = "Last Name"
                    case "3":
                        value_type_list[index] = "Full Name"
                    case _:
                        msg_print.err_panel(const['ERROR_WRONG_MENU'])
            case "number" | "num":
                value_type_list[index] = "Number"
            case "tel" | "t":
                value_type_list[index] = "Tel"
            case "email" | "e":
                value_type_list[index] = "E-Mail"
            case "percentage" | "per" | "p":
                value_type_list[index] = "Percentage"
            case "boolean" | "bool" | "b":
                value_type_list[index] = "Boolean"
            case "list" | "li" | "l":
                msg_print.display_list_type()
                list_type = input(">> ")
                match list_type:
                    case '1':
                        value_type_list[index] = "List(String)"
                    case '2':
                        value_type_list[index] = "List(Number)"
                    case '3':
                        value_type_list[index] = "List(Name)"
                    case '4':
                        value_type_list[index] = "List(E-Mail)"
                    case '5':
                        value_type_list[index] = "List(Tel)"
                    case _:
                        msg_print.err_panel("SELECT CORRECT MENU")

            # case "object" | "obj" | "o":
            #     value_type_list[index] = "Object"
            case _:
                msg_print.err_panel("SELECT CORRECT MENU")
    create_json_data(keys, value_type_list)


def create_json_data(keys, value_type_list):
    json_data = {}
    index = 0
    for key in keys:
        data = ""
        match value_type_list[index]:
            case "List(String)":
                msg_print.msg_panel(const['REQUIRE_VALUE_COUNT'], '')
                list_cnt = input(">> ")
                data = random_list.create_random_list('str', list_cnt)
            case "List(Number)":
                msg_print.msg_panel(const['REQUIRE_VALUE_COUNT'], '')
                list_cnt = input(">> ")
                data = random_list.create_random_list('number', list_cnt)
            case "List(Name)":
                msg_print.msg_panel(const['REQUIRE_VALUE_COUNT'], '')
                list_cnt = input(">> ")
                data = random_list.create_random_list('name', list_cnt)
            case "List(E-Mail)":
                msg_print.msg_panel(const['REQUIRE_VALUE_COUNT'], '')
                list_cnt = input(">> ")
                data = random_list.create_random_list('email', list_cnt)
            case "List(Tel)":
                msg_print.msg_panel(const['REQUIRE_VALUE_COUNT'], '')
                list_cnt = input(">> ")
                data = random_list.create_random_list('tel', list_cnt)
            case "First Name":
                data = random_names.create_random_name("first")
                first_name = data
            case "Last Name":
                data = random_names.create_random_name("last")
                last_name = data
            case "Full Name":
                if "First Name" in value_type_list and "Last Name" in value_type_list:
                    data = first_name + " " + last_name
                else:
                    data = random_names.create_random_name("full")
            case "Number":
                data = random_numbers.create_random_number()
            case "Tel":
                data = random_tel_nums.create_tel_number()
            case "E-Mail":
                data = random_email.create_email_address()
            case "Percentage":
                data = str(random.randint(0, 100)) + "%"
            case "Boolean":
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
