from string import ascii_letters, digits
from random import sample
password_string = ''.join(set(ascii_letters) | set(digits) - set('lIoO01'))


def generate_password(length):
    return ''.join(sample(password_string, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


print(*generate_passwords(int(input()), int(input())), sep='\n')
