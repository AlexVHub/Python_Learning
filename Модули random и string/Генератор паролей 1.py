from string import ascii_letters, digits
from random import sample


def generate_password(length):
    password_string = ''.join(i for i in (ascii_letters + digits) if i not in 'lIoO01')
    return ''.join(sample(password_string, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


print(*generate_passwords(int(input()), int(input())), sep='\n')
