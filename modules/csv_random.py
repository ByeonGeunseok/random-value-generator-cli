import time
import os
from . import random_names
from . import random_numbers
from . import random_tel_nums
from . import random_email
import csv


global headers
headers = []
global col_type_contents
col_type_contents = []
global col_type_list
col_type_list = []


def set_config_header():
    while True:
        print("-*- -*- -*- -*- -*- -*- -*-")
        print("If you need header, input once.")
        print("If you delete to last header, input \" \" and ENTER.")
        print("if you done to input header, Just press ENTER.")
        print("-*- -*- -*- -*- -*- -*- -*-")
        if len(headers) <= 0:
            print("header: (nothing)")
        else:
            print("header: ", *headers)
        print("-*- -*- -*- -*- -*- -*- -*-")

        header_str = input()

        if header_str == " ":
            # Delete last header
            if len(headers) <= 0:
                print("There are no headers.")
            else:
                headers.pop()
        elif header_str == "":
            break
        else:
            headers.append(header_str)
    set_config_column_type(headers)
    create_csv()


def set_config_column_type(headers):
    col_cnt = len(headers)

    if col_cnt <= 0:
        continue_flg = input(
            "There are no headers. Are you continue to create CSV? [y/n]")
        if continue_flg == "y":
            col_cnt = int(input("How many columns do you need?"))

    for i in range(col_cnt):
        print("What type of column of ", headers[i])
        col_type = input(
            "[name/number/num/tel/email/percentage/per/boolean/bool]")
        if col_type == "name":
            col_type = random_names.choose_name_type()
        col_type_list.append(col_type)


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
                    random_tel_nums.generate_fake_phone_number())

            case "email":
                col_type_contents.append(random_email.create_email_address())
            case "percentage":
                print()
            case "boolean":
                print()
            case _:
                print()
    return col_type_contents


def create_csv():
    current_time = time.strftime('%Y%m%d%H%M%S')
    path = "./output/"
    file_name = path + "random_" + current_time + ".csv"
    cnt = int(input("How many rows do you need? : "))

    # folder check
    if os.path.isdir("./output") == False:
        os.mkdir("./output")
    file = open(file_name, 'w', newline='')
    wr = csv.writer(file)
    wr.writerow(headers)

    for _ in range(cnt):
        wr.writerow(create_csv_row(col_type_list))

    file.close()
