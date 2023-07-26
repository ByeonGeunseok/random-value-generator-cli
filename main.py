from modules.menus import *
from modules.utils import error_check
from modules.utils import msg_print
from const import const

while True:
    # START
    msg_print.render_main_menu()
    # Choose the menu, Return menu number.
    menu = input(const['REQUIRE_MENU'])

    # Check the input.
    if menu.isdigit():
        msg_print.clear_screen()

        # Choose the menu
        match menu:
            # Repeat Menu
            case "1":
                number_repeat.execute_number_repeat()
            # Shuffle menu
            case "2":
                number_shuffle.execute_number_shuffle()
            # Random string menu
            case "3":
                string_random.execute_random_string()
            # Random CSV menu
            case "4":
                csv_random.set_csv_header()
            # Random JSON menu
            case "5":
                json_random.set_json_key()
            # End
            case "9":
                break
            # If the menu doesn't exist.
            case _:
                error_check.err_panel(const['ERROR_WRONG_MENU'])
    # If input is not number.
    else:
        error_check.err_panel(const['ERROR_WRONG_MENU'])
