import random

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


def create_random_name(list):
    # Create the random name
    print("First name [1]")
    print("Last name [2]")
    print("Full name [3]")
    name_type = input("Choose : ")
    if name_type == "1":
        list.append(random.choice(first_names))
    elif name_type == "2":
        list.append(random.choice(last_names))
    elif name_type == "3":
        list.append(random.choice(first_names) +
                    " " + random.choice(last_names))
    else:
        return 0
    return list
