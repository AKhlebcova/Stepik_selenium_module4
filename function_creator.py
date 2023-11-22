import secrets
import string
import time


def get_random_email():
    email = str(time.time()) + "@fakemail.org"
    return email


def get_random_password():
    alphabet = string.ascii_letters + string.digits
    secret_key = ''
    for i in range(9):
        secret_key += ''.join(secrets.choice(alphabet))
    return secret_key
