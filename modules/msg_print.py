import os
import platform
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from config import config


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def render_main_menu():
    table = Table(title=config['REQUIRE_MENU'],
                  show_header=True, header_style="bold")
    table.add_column("SELECT")
    table.add_column("TYPE")
    table.add_column("DESCRIPTION")
    table.add_row("Press [1]", "Number Repeat", "")
    table.add_row("Press [2]", "Number Shuffle", "")
    table.add_row("Press [3]", "Random String", "")
    table.add_row("Press [4]", "Random CSV", "")
    table.add_row("Press [5]", "Random JSON", "")
    table.add_row()
    table.add_row("Press [9]", "EXIT...", "")

    clear_screen()
    console = Console()
    console.print(table, justify="center")


def display_repeat_count(result, amount):
    console = Console()

    table = Table(title="NUMBER COUNT",
                  show_header=True, header_style="bold")
    table.add_column("NUMBER")
    table.add_column("COUNT")

    for i in range(amount):
        num, cnt = result[i]
        table.add_row(str(num), str(cnt))

    console.print(table)


def display_string_menu(length, number_state, lower_state, upper_state, punctuation_state):
    console = Console()

    table = Table(title=config['REQUIRE_MENU'],
                  show_header=True, header_style="bold")
    table.add_column("SELECT")
    table.add_column("TYPE")
    table.add_column("STATE")
    table.add_row("Press [1]", "String Length", str(length))
    table.add_row("Press [2]", "Use Number", number_state)
    table.add_row("Press [3]", "Use Lower Case", lower_state)
    table.add_row("Press [4]", "Use Upper Case", upper_state)
    table.add_row("Press [5]", "Use Punctuation", punctuation_state)
    table.add_row()
    table.add_row("Press [9]", "EXECUTE", "")
    table.add_row("Press [0]", "DONE", "")

    console.print(table)


def msg_panel(msg, title):
    print(Panel(msg, title=title, style="bold"))


def err_panel(msg):
    print(Panel(msg, title="ERROR", style="bold red"))


def result_panel(msg):
    print(Panel(msg, title="RESULT", style="bold green"))


def display_name_type():
    console = Console()

    table = Table(title=config['REQUIRE_MENU'],
                  show_header=True, header_style="bold")
    table.add_column("SELECT")
    table.add_column("TYPE")
    table.add_row("Press [1]", "First Name")
    table.add_row("Press [2]", "Last Name")
    table.add_row("Press [3]", "Full Name")

    console.print(table)


def display_json_type(keys, list):
    index = 0
    json_length = len(keys)
    console = Console()

    table = Table(title=config['REQUIRE_MENU'],
                  show_header=True, header_style="bold")

    table.add_column("SELECT")
    table.add_column("KEY")
    table.add_column("TYPE")

    for key in keys:
        table.add_row(f"Type [{index+1}]", key, f"{list[index]}")
        index += 1
    table.add_row()
    table.add_row("Press [ENTER]", "NEXT", "")

    console.print(table)

    return list
