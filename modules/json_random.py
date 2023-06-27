from modules.msg_print import *

global keys
global value_type_list
keys = []
value_type_list = []


def set_config_key():
    while True:
        msg = "Input a key.\n" + \
            "If you delete to last key, input \" \" and ENTER.\n" + \
            "If you done to input key, Just press ENTER."
        title = "Random CSV"
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
    for i in range(len(keys)):
        value_type_list.append("X")

    while True:
        value_type_list = msg_json_type(keys, value_type_list)
        select = input("Change value type >> ")

        if select == "":
            break
        elif int(select) <= len(keys):
            type = value_type_list[int(select)-1]
            if type == "O":
                value_type_list[int(select)-1] = "X"
            else:
                value_type_list[int(select)-1] = "O"
