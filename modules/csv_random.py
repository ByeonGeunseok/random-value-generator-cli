import time
import os
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
global col_type_list
col_type_list = []


def set_config_header():
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
    set_config_column_type(headers)


def set_config_column_type(headers):
    col_cnt = len(headers)

    if col_cnt <= 0:
        msg = "There are no headers. Are you continue to create CSV?"
        title = "Random CSV"
        msg_panel(msg, title)
        continue_flg = input("(y/n) >>")
        if continue_flg == "y":
            msg = "How many columns do you need?"
            title = "Random CSV"
            msg_panel(msg, title)
            col_cnt = int(input(">>"))
        else:
            return

    for i in range(col_cnt):
        msg = "What type of column of " + \
            headers[i] + "\n" + \
            "(name/number/num/tel/email/percentage/per/boolean/bool)"
        title = "Random CSV"
        msg_panel(msg, title)

        col_type = input(">>")
        if col_type == "name":
            col_type = random_names.choose_name_type()
        col_type_list.append(col_type)

    create_csv(headers, col_type_list)


def create_csv_row(col_type_list):
    col_type_contents = []
    for col_type in col_type_list:
        match col_type:
            case "name_first":
                col_type_contents.append(
                    random_names.create_random_name("first"))

            case "name_last":
                col_type_contents.append(
                    random_names.create_random_name("last"))

            case "name_full":
                if ("name_first" in col_type_list) & ("name_last" in col_type_list):
                    name_full = col_type_contents[col_type_list.index(
                        "name_first")] + " " + col_type_contents[col_type_list.index("name_last")]
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


def create_csv(headers, col_type_list):
    current_time = time.strftime('%Y%m%d%H%M%S')
    path = conf['OUTPUT_PATH']
    file_name = path + "random_" + current_time + ".csv"
    cnt = int(input(f"{const['REQUIRE_ROW_COUNT']} : "))

    # folder check
    if os.path.isdir(conf['OUTPUT_PATH']) == False:
        os.mkdir(conf['OUTPUT_PATH'])
    file = open(file_name, 'w', newline='')
    wr = csv.writer(file)
    wr.writerow(headers)

    for _ in range(cnt):
        wr.writerow(create_csv_row(col_type_list))

    file.close()
