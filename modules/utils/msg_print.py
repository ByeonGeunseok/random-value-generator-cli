from os import system
from platform import system as plsys
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from const import const


def clear_screen():
    """
    Clear the console screen.
    """
    if plsys() == "Windows":
        system("cls")
    else:
        system("clear")


def render_main_menu():
    """
    Render the main menu.
    """
    table = Table(title=const['REQUIRE_MENU'],
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

    console.print(table, justify="center")


def display_string_menu(length, number_state, lower_state, upper_state, punctuation_state):
    console = Console()

    table = Table(title=const['REQUIRE_MENU'],
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
    table.add_row("Press [0]", "QUIT", "")

    console.print(table, justify="center")


def msg_panel(msg, *title):
    if title:
        print(Panel(msg, title=title[0], style="bold"))
    else:
        print(Panel(msg, style="bold"))


def err_panel(msg):
    print(Panel(msg, title="ERROR", style="bold red"))


def result_panel(msg):
    print(Panel(msg, title="RESULT", style="bold green"))


def display_name_type():
    console = Console()

    table = Table(title=const['REQUIRE_MENU'],
                  show_header=True, header_style="bold")
    table.add_column("SELECT")
    table.add_column("TYPE")
    table.add_row("Press [1]", "First Name")
    table.add_row("Press [2]", "Last Name")
    table.add_row("Press [3]", "Full Name")

    console.print(table, justify="center")


def display_list_type():
    console = Console()

    table = Table(title=const['REQUIRE_MENU'],
                  show_header=True, header_style="bold")
    table.add_column("SELECT")
    table.add_column("TYPE")
    table.add_row("Press [1]", "String")
    table.add_row("Press [2]", "Number")
    table.add_row("Press [3]", "Name")
    table.add_row("Press [4]", "E-Mail")
    table.add_row("Press [5]", "Tel")

    console.print(table, justify="center")


def display_csv_type(keys, list):
    index = 0
    json_length = len(keys)
    console = Console()

    table = Table(title=const['REQUIRE_MENU'],
                  show_header=True, header_style="bold")

    table.add_column("SELECT")
    table.add_column("KEY")
    table.add_column("TYPE")

    for key in keys:
        table.add_row(f"Type [{index+1}]", key, f"{list[index]}")
        index += 1
    table.add_row()
    table.add_row("Press [ENTER]", "NEXT", "")

    console.print(table, justify="center")

    return list


def display_json_type(keys, list):
    index = 0
    json_length = len(keys)
    console = Console()

    table = Table(title=const['REQUIRE_MENU'],
                  show_header=True, header_style="bold")

    table.add_column("SELECT")
    table.add_column("KEY")
    table.add_column("TYPE")

    for key in keys:
        table.add_row(f"Type [{index+1}]", key, f"{list[index]}")
        index += 1
    table.add_row()
    table.add_row("Press [ENTER]", "NEXT", "")

    console.print(table, justify="center")

    return list


def check_continue():
    print(Panel(const['REQUIRE_CONTINUE'], style="bold"))
    temp = input()


def display_type_selector(type):
    def get_content(menus):
        return f"[b]{menus['name']}[/b]\n[yellow]{menus['keyword']}"

    console = Console()

    menus = [{
        'name': 'Name',
        'keyword': 'name / na'
    }, {
        'name': 'Number',
        'keyword': 'number / num',
    }, {
        'name': 'Tel',
        'keyword': 'tel / t',
    }, {
        'name': 'E-Mail',
        'keyword': 'email / e',
    }, {
        'name': 'Percent',
        'keyword': 'percent / per / p',
    }, {
        'name': 'Boolean',
        'keyword': 'boolean / bool / b',
    }]

    extra = [{
        'name': 'List',
        'keyword': 'list / li / l',
    }, {
        'name': 'Object',
        'keyword': 'object / obj / o',
    }]

    if type == 'json':
        menus = menus + extra

    # console.print(menus, overflow="ignore", crop=False)
    menu_renderables = [Panel(get_content(menu), expand=True)
                        for menu in menus]
    console.print(Columns(menu_renderables))
