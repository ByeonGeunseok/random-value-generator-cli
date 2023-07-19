from modules.menus.string_random import create_value


def create_email_address():
    EMAIL_AT = "@"
    EMAIL_TAIL = ".com"
    LENGTH = 8

    email_id = create_value(LENGTH, True, True, False, False)
    email_address = create_value(LENGTH, True, True, False, False)

    email_string = email_id + EMAIL_AT + email_address + EMAIL_TAIL

    return email_string
