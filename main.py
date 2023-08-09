from modules.menus import *
from modules.utils import error_check
from modules.utils import msg_print
from message import message

is_error = False

while True:
    msg_print.clear_screen()

    if is_error:
        error_check.err_panel(message['ERROR_WRONG_MENU'])
        is_error = False

    # START
    msg_print.render_main_menu()
    # Choose the menu, Return menu number.
    menu = input(message['REQUIRE_MENU'])

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
                is_error = True
    # If input is not number.
    else:
        is_error = True
