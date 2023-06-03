from string import ascii_letters, digits
from random import *
password_string = ''.join(i for i in ascii_letters + digits if i not in 'lIoO01')


def generate_password(length):
    password = list(choice(password_string[:24]) + choice(password_string[24:48]) + choice(password_string[48:]) + ''.join(sample(password_string, length - 3)))
    shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


print(*generate_passwords(int(input()), int(input())), sep='\n')
