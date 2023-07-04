from modules.number_repeat import *
from modules.number_shuffle import *
from modules.string_random import *
from modules.csv_random import *
from modules.json_random import *
from modules.error_check import *
from modules.msg_print import *
from const import const

while True:
    # START
    render_main_menu()

    # Choose the menu, Return menu number.
    menu = input(const['REQUIRE_MENU'])

    # Check the input.
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
                set_csv_header()
            # Random JSON menu
            case "5":
                set_json_key()
            # End
            case "9":
                break
            # If the menu doesn't exist.
            case _:
                err_panel(const['ERROR_WRONG_MENU'])
    # If input is not number.
    else:
        err_panel(const['ERROR_WRONG_MENU'])
