from random import choice
from string import ascii_letters


def create_email_address():
    email_id = ""
    email_address = ""
    EMAIL_AT = "@"
    EMAIL_TAIL = ".com"
    LENGTH = 8

    val = ascii_letters
    for _ in range(LENGTH):
        email_id += choice(val)
        email_address += choice(val)

    email_string = email_id + EMAIL_AT + email_address + EMAIL_TAIL

    return email_string
