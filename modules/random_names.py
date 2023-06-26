import random
from modules.msg_print import msg_name_type

first_names = [
    "Liam", "Ava", "Noah", "Isabella", "Ethan", "Sophia", "Mason", "Mia", "Lucas", "Charlotte",
    "Oliver", "Amelia", "Elijah", "Harper", "Aiden", "Evelyn", "James", "Abigail", "Benjamin", "Emily",
    "Henry", "Elizabeth", "Alexander", "Sofia", "William", "Avery", "Daniel", "Ella", "Samuel", "Scarlett",
    "Michael", "Grace", "Matthew", "Victoria", "Jackson", "Chloe", "Sebastian", "Camila", "David", "Zoey",
    "Carter", "Penelope", "Jayden", "Riley", "Joseph", "Layla", "John", "Lillian", "Gabriel", "Natalie"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
    "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
    "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Young", "Hall", "Walker", "Allen",
    "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Adams", "Nelson", "Baker", "Hall",
    "Rivera", "Mitchell", "Carter", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards"
]


def choose_name_type():
    msg_name_type()
    name_type = input("Choose : ")

    match name_type:
        case "1":
            return f"name_first"
        case "2":
            return f"name_last"
        case "3":
            return f"name_full"
        case _:
            return f"name_full"


def create_random_name(name_type):
    if name_type == "first":
        return random.choice(first_names)
    elif name_type == "last":
        return random.choice(last_names)
    elif name_type == "full":
        full_name = random.choice(first_names) + " " + \
            random.choice(last_names)
        return full_name
    else:
        return 0
