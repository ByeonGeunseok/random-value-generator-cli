from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table


def msg_main_menu():
    console = Console()

    table = Table(title="CHOOSE THE MENU",
                  show_header=True, header_style="bold")
    table.add_column("SELECT")
    table.add_column("TYPE")
    table.add_row("Press [1]", "Number Repeat")
    table.add_row("Press [2]", "Number Shuffle")
    table.add_row("Press [3]", "Random String")
    table.add_row("Press [4]", "Random CSV")
    table.add_row()
    table.add_row("Press [9]", "EXIT...")

    console.print(table)


def msg_string_menu(length, number_state, lower_state, upper_state, punctuation_state):
    console = Console()

    table = Table(title="CHOOSE THE MENU",
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
    print(Panel(msg, title="Random CSV"))


def msg_name_type():
    console = Console()

    table = Table(title="CHOOSE THE MENU",
                  show_header=True, header_style="bold")
    table.add_column("SELECT")
    table.add_column("TYPE")
    table.add_row("Press [1]", "First Name")
    table.add_row("Press [2]", "Last Name")
    table.add_row("Press [3]", "Full Name")

    console.print(table)