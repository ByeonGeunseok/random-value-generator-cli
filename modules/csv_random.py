import sys
sys.path.append(r'./modules/variables/')
import var_names
import var_numbers
import var_tel_nums


global col_type_contents
col_type_contents = []
global headers
headers = []


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

        match col_type:
            case "name":
                col_type_contents.append(
                    var_names.create_random_name(col_type_contents))
                print(col_type_contents)
            case "number" | "num":
                col_type_contents.append(var_numbers.create_random_number())
                print(col_type_contents)
            case "tel":
                col_type_contents.append(
                    var_tel_nums.generate_fake_phone_number())
                print(col_type_contents)
                print()
            case "email":
                print()
            case "percentage":
                print()
            case "boolean":
                print()
            case _:
                print("What?")


set_config_header()