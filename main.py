from modules.number_repeat import *
from modules.number_shuffle import *
from modules.string_random import *
from modules.csv_random import *
from modules.json_random import *
from modules.error_check import *
from modules.msg_print import *
from const import const

while 1:
    is_possible = True

    # START
    render_main_menu()

    menu = input(const['REQUIRE_MENU'])

    if menu.isdigit():
        clear_screen()

        # Choose the menu
        match menu:
            # Repeat Menu
            case "1":
                execute_number_repeat()
            # Shuffle menu
            case "2":
                execute_number_shuffle()
            # Random string menu
            case "3":
                execute_random_string()
            # Random CSV menu
            case "4":
                set_config_header()
            # Random JSON menu
            case "5":
                set_config_key()
            case "9":
                break
            case _:
                err_panel(const['ERROR_WRONG_MENU'])
    else:
        err_panel(const['ERROR_WRONG_MENU'])
