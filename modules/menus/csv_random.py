from pathlib import Path
import time
import random
import csv
from conf import conf
from const import const
from ..utils import *


def set_csv_header():
    error_flg = False
    quit_flg = False
    headers = []

    while True:
        msg = "If you need header, input once.\n" + \
            "If you delete to last header, input \" \" and ENTER.\n" + \
            "If you done to input header, Just press ENTER.\n" + \
            "If you want to quit, input \"!q\" and ENTER."
        title = "Random CSV"
        msg_print.msg_panel(msg, title)

        if len(headers) <= 0:
            msg_print.msg_panel("header: (nothing)")
        else:
            msg_print.msg_panel(f"header: {headers}")
        if error_flg:
            msg_print.err_panel(const['ERROR_NO_HEADER'])
            error_flg = False
        header_str = input()

        if header_str == " ":
            if len(headers) <= 0:
                error_flg = True
            else:
                headers.pop()
        elif header_str == "":
            break
        elif header_str == "!q":
            quit_flg = True
            break
        else:
            headers.append(header_str)
        msg_print.clear_screen()
    if not quit_flg:
        set_column_type(headers)


def set_column_type(headers):
    value_type_list = []
    col_cnt = len(headers)

    if col_cnt <= 0:
        msg = "There are no headers. Are you continue to create CSV?"
        title = "Random CSV"
        msg_print.msg_panel(msg, title)
        continue_flg = input("(y/n) >>")
        if continue_flg == "y":
            title = "Random CSV"
            msg_print.msg_panel(const['REQUIRE_COLUMN_COUNT'], title)
            col_cnt = int(input(">>"))

            for _ in range(col_cnt):
                headers.append("")
        else:
            return

    for _ in range(col_cnt):
        value_type_list.append("")

    while True:
        value_type_list = msg_print.display_csv_type(headers, value_type_list)
        menu = input("Choose the menu >> ")
        if menu == "":
            break
        elif menu.isdigit():
            if int(menu) <= col_cnt and menu != "0":
                index = int(menu) - 1
            else:
                msg_print.err_panel(const['ERROR_WRONG_MENU'])
                continue
        else:
            msg_print.err_panel(const['ERROR_WRONG_MENU'])
            continue

        msg_print.display_type_selector('csv')
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
            case _:
                msg_print.err_panel(const['ERROR_WRONG_MENU'])

    create_csv(headers, value_type_list)


def create_csv_row(value_type_list):
    col_type_contents = []
    for col_type in value_type_list:
        match col_type:
            case "First Name":
                col_type_contents.append(
                    random_names.create_random_name("first"))

            case "Last Name":
                col_type_contents.append(
                    random_names.create_random_name("last"))

            case "Full Name":
                if ("First Name" in value_type_list) & ("Last Name" in value_type_list):
                    name_full = col_type_contents[value_type_list.index(
                        "First Name")] + " " + col_type_contents[value_type_list.index("Last Name")]
                    col_type_contents.append(name_full)
                else:
                    col_type_contents.append(
                        random_names.create_random_name("full"))

            case "Number":
                col_type_contents.append(random_numbers.create_random_number())

            case "Tel":
                col_type_contents.append(
                    random_tel_nums.create_tel_number())

            case "E-Mail":
                col_type_contents.append(random_email.create_email_address())
            case "Percentage":
                percent = str(random.randint(0, 100)) + "%"
                col_type_contents.append(percent)
            case "Boolean":
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
