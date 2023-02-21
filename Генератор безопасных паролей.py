import random

DIGITS = '0123456789'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION = '!#$%&*+-=?@^_'
AMBIGUOUS = 'il1Lo0O'

chars = ''

count = int(input('Введите количество паролей для генерации?', ))
length = int(input('Введите длину одного пароля?', ))
include_digits = input('Включать ли цифры 0123456789? д(да) или н(нет)', )
include_uppercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д(да) или н(нет)', )
include_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д(да) или н(нет)', )
include_punctuation = input('Включать ли символы !#$%&*+-=?@^_? д(да) или н(нет)', )
exclude_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O? д(да) или н(нет)', )

if include_digits == 'д' or include_digits == 'да':
    chars += DIGITS
if include_uppercase == 'д' or include_uppercase == 'да':
    chars += UPPERCASE_LETTERS
if include_lowercase == 'д' or include_lowercase == 'да':
    chars += LOWERCASE_LETTERS
if include_punctuation == 'д' or include_punctuation == 'да':
    chars += PUNCTUATION
if exclude_ambiguous == 'д' or exclude_ambiguous == 'да':
    for i in AMBIGUOUS:
        chars = chars.replace(i, '')

def generate_password(length, chars):
    return random.sample(chars, length)

for _ in range(count):
    print(*generate_password(length, chars), sep='')