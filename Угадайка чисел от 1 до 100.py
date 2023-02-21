import random

print('Добро пожаловать в числовую угадайку')

def is_valid(a):
    if a.isdigit() and 0 < int(a) <= int(right):
        return True
    else:
        return False

while True:
    right = input('Введите правую границу диапазона?', )
    if is_valid(right) == False:
        print('А может быть все-таки введем целое число для правой границы?')
        continue
    right = int(right)
    n = random.randint(1, right)
    count = 0
    print('Я загадал число от 1 до', right, 'попробуйте угадать его :)')

    while True:
        print('Введите число от 1 до', right, ';)')
        a = input()
        if is_valid(a) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        a = int(a)
        count += 1
        if a < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif a > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif a == n:
            print('Вы угадали за', count, 'попыток, поздравляем!')
            break

    repeat = input('Хотите сыграть ещё?, введите д(да) или н(нет)', )
    if repeat == 'д' or repeat == 'да':
        continue
    else:
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')