from pathlib import Path
from json import *
import random
import re
import time
from conf import conf
from message import message
from ..utils import random_list
from ..utils import msg_print
from ..utils import random_names
from ..utils import random_numbers
from ..utils import random_tel_nums
from ..utils import random_email


def set_json_key():
    error_flg = False
    quit_flg = False
    keys = []

    while True:
        if error_flg:
            msg_print.err_panel(message['ERROR_NO_KEY'])
            error_flg = False

        msg = "Input a key.\n" + \
            "If you delete to last key, input \" \" and ENTER.\n" + \
            "If you done to input key, Just press ENTER.\n" + \
            "If you want to quit, input \"!q\" and ENTER."
        title = "Random JSON"
        msg_print.msg_panel(msg, title)

        if len(keys) <= 0:
            msg_print.msg_panel("key: (nothing)")
        else:
            msg_print.msg_panel(f"key: {keys}")

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
        elif key_str == "!q":
            quit_flg = True
            break
        else:
            keys.append(key_str)
        msg_print.clear_screen()
    if not quit_flg:
        set_key_type(keys)


# TODO: Add a object
# TODO: Modify the logic about setting variables and list row count
def set_key_type(keys):
    json_list = {}
    list_id = 0
    error_index = ''
    value_type_list = []
    data_length = len(keys)
    for _ in range(data_length):
        value_type_list.append("")

    for key in keys:
        json_list[list_id] = [key, 0]
        list_id += 1

    while True:
        msg_print.clear_screen()
        if not error_index == '':
            msg_print.err_panel(message[error_index])
            error_index = ''
        value_type_list = msg_print.display_json_type(keys, value_type_list)
        menu = input(f"{message['REQUIRE_MENU']} >> ")
        if menu == "":
            if '' in value_type_list:
                error_index = 'ERROR_INPUT'
                continue
            else:
                break
        elif menu.isdigit():
            if int(menu) <= data_length and menu != "0":
                index = int(menu) - 1
            else:
                error_index = 'ERROR_WRONG_MENU'
                continue
        else:
            error_index = 'ERROR_WRONG_MENU'
            continue

        msg_print.display_type_selector('json')
        select_type = input(">> ")

        match select_type:
            case "name" | "na":
                msg_print.clear_screen()
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
                        error_index = 'ERROR_WRONG_MENU'
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
                msg_print.clear_screen()
                msg_print.display_list_type()
                list_type = input(">> ")
                msg_print.clear_screen()
                msg_print.msg_panel(message['REQUIRE_VALUE_COUNT'], '')
                list_cnt = input(">> ")
                match list_type:
                    case '1':
                        value_type_list[index] = "List(String)" + list_cnt
                    case '2':
                        value_type_list[index] = "List(Number)" + list_cnt
                    case '3':
                        value_type_list[index] = "List(Name)" + list_cnt
                    case '4':
                        value_type_list[index] = "List(E-Mail)" + list_cnt
                    case '5':
                        value_type_list[index] = "List(Tel)" + list_cnt
                    case _:
                        error_index = 'ERROR_WRONG_MENU'

            # case "object" | "obj" | "o":
            #     value_type_list[index] = "Object"
            case _:
                error_index = 'ERROR_WRONG_MENU'
    create_json_data(keys, value_type_list)


def create_json_data(keys, value_type_list):
    json_data = {}
    index = 0
    for key in keys:
        data = ""
        match value_type_list[index]:
            case value if "List" in value_type_list[index]:

                list_type = slice_string("bracket", value)
                match list_type[0]:
                    case "String":
                        list_cnt = slice_string("tail", value)
                        data = random_list.create_random_list(
                            'str', list_cnt[0])
                    case "Number":
                        list_cnt = slice_string("tail", value)
                        data = random_list.create_random_list(
                            'number', list_cnt[0])
                    case "Name":
                        list_cnt = slice_string("tail", value)
                        data = random_list.create_random_list(
                            'name', list_cnt[0])
                    case "E-Mail":
                        list_cnt = slice_string("tail", value)
                        data = random_list.create_random_list(
                            'email', list_cnt[0])
                    case "Tel":
                        list_cnt = slice_string("tail", value)
                        data = random_list.create_random_list(
                            'tel', list_cnt[0])
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


def slice_string(course, input):
    result = ""
    match course:
        case "bracket":
            result = re.findall(r"\((.*?)\)", input)
        case "tail":
            result = re.findall(r"\)(.*?)$", input)
    return result
