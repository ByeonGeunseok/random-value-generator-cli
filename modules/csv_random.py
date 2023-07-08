from pathlib import Path
import time
from . import random_names
from . import random_numbers
from . import random_tel_nums
from . import random_email
import random
import csv
from modules.msg_print import *
from conf import conf
from const import const

global headers
headers = []
global col_type_contents
col_type_contents = []


def set_csv_header():
    headers = []
    while True:
        msg = "If you need header, input once.\n" + \
            "If you delete to last header, input \" \" and ENTER.\n" + \
            "If you done to input header, Just press ENTER."
        title = "Random CSV"
        msg_panel(msg, title)

        if len(headers) <= 0:
            msg_panel("header: (nothing)", "HEADER")
        else:
            msg_panel(f"header: {headers}", "HEADER")
        header_str = input()

        if header_str == " ":
            # Delete last header
            if len(headers) <= 0:
                err_panel(const['ERROR_NO_HEADER'])
            else:
                headers.pop()
        elif header_str == "":
            break
        else:
            headers.append(header_str)
    set_column_type(headers)


def set_column_type(headers):
    value_type_list = []
    col_cnt = len(headers)

    if col_cnt <= 0:
        msg = "There are no headers. Are you continue to create CSV?"
        title = "Random CSV"
        msg_panel(msg, title)
        continue_flg = input("(y/n) >>")
        if continue_flg == "y":
            title = "Random CSV"
            msg_panel(const['REQUIRE_COLUMN_COUNT'], title)
            col_cnt = int(input(">>"))

            for _ in range(col_cnt):
                headers.append("")
        else:
            return

    for _ in range(col_cnt):
        value_type_list.append("")

    while True:
        value_type_list = display_csv_type(headers, value_type_list)
        menu = input("Choose the menu >> ")
        if menu == "":
            break
        elif menu.isdigit():
            if int(menu) <= col_cnt and menu != "0":
                index = int(menu) - 1
            else:
                err_panel(const['ERROR_WRONG_MENU'])
                continue
        else:
            err_panel(const['ERROR_WRONG_MENU'])
            continue

        msg_panel(
            f"((name/number/num/tel/email/percentage/per/boolean/bool))", "TYPE SELECT")
        select_type = input(">> ")

        if select_type == "list":
            value_type_list[index] = select_type
        elif select_type == "name":
            display_name_type()
            name_menu = input(">> ")
            if name_menu == "1":
                value_type_list[index] = "first name"
            elif name_menu == "2":
                value_type_list[index] = "last name"
            elif name_menu == "3":
                value_type_list[index] = "full name"
            else:
                err_panel(const['ERROR_WRONG_MENU'])
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
            err_panel(const['ERROR_WRONG_MENU'])

    create_csv(headers, value_type_list)


def create_csv_row(value_type_list):
    col_type_contents = []
    for col_type in value_type_list:
        match col_type:
            case "first name":
                col_type_contents.append(
                    random_names.create_random_name("first"))

            case "last name":
                col_type_contents.append(
                    random_names.create_random_name("last"))

            case "full name":
                if ("first name" in value_type_list) & ("last name" in value_type_list):
                    name_full = col_type_contents[value_type_list.index(
                        "first name")] + " " + col_type_contents[value_type_list.index("last name")]
                    col_type_contents.append(name_full)
                else:
                    col_type_contents.append(
                        random_names.create_random_name("full"))

            case "number" | "num":
                col_type_contents.append(random_numbers.create_random_number())

            case "tel":
                col_type_contents.append(
                    random_tel_nums.create_tel_number())

            case "email":
                col_type_contents.append(random_email.create_email_address())
            case "percentage" | "per":
                percent = str(random.randint(0, 100)) + "%"
                col_type_contents.append(percent)
            case "boolean" | "bool":
                col_type_contents.append(bool(random.getrandbits(1)))
            case _:
                print()
    return col_type_contents


def create_csv(headers, value_type_list):
    current_time = time.strftime('%Y%m%d%H%M%S')
    path = conf['OUTPUT_PATH']
    file_name = path + "random_" + current_time + ".csv"
    cnt = int(input(f"{const['REQUIRE_ROW_COUNT']} : "))

    Path(path).mkdir(exist_ok=True)
    file = open(file_name, 'w', newline='')
    wr = csv.writer(file)
    wr.writerow(headers)

    for _ in range(cnt):
        wr.writerow(create_csv_row(value_type_list))

    file.close()
