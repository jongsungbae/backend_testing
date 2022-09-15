import logging as logger
import random
import string

def generate_random_email(domain=None, email_prefix=None):
    if not domain:
        domain = 'test.com'
    if not email_prefix:
        email_prefix = 'testUser'

    random_email_string_length = 5
    string_pool = string.ascii_lowercase
    random_string = ''.join(random.choices(string_pool, k=random_email_string_length))

    email_string = f'{email_prefix}_{random_string}@{domain}'

    logger.debug(f'random email: {email_string}')
    return email_string

def generate_random_password():
    password_length = 10
    string_pool = string.ascii_letters
    password_string = ''.join(random.choices(string_pool, k=password_length))

    logger.debug(f'random password: {password_string}')
    return password_string
