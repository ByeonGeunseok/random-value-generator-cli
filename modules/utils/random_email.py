import random
import string


def create_email_address():
    EMAIL_AT = "@"
    EMAIL_TAIL = ".com"
    LENGTH = 8

    val = string.ascii_letters
    for _ in range(LENGTH):
        email_id = random.choice(val)
        email_address = random.choice(val)

    email_string = email_id + EMAIL_AT + email_address + EMAIL_TAIL

    return email_string
