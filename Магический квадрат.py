# Магическим квадратом порядка n называется квадратная таблица размера n×n, так, что суммы по каждому столбцу, каждой
# строке и каждой из двух диагоналей равны между собой. Программа проверяет, является ли заданная квадратная матрица
# магическим квадратом.
def magic_square_check(matrix, summa):  # Функция проверки является ли матрица магически квадратом
    global flag
    diagonal = 0
    for i in range(n):
        if sum(matrix[i]) != summa:  # Проверка равна ли строка параметру summa
            flag = 'NO'
            break
        for j in range(n):
            if i == j:
                diagonal += matrix[j][i]
    if diagonal != summa:  # Проверка равна ли главная диагональ параметру summa
        flag = 'NO'
    return flag


n = int(input())  # Размерность матрицы
matrix = [[int(i) for i in input().split()] for _ in range(n)]  # Ввод матрицы
rotate_matrix = []  # Загатовка перевернутой матрицы
summa = sum(matrix[0])  # Сумма элементов первой строки матрицы
flag = 'YES'  # Признак наличия магического квадрата

for i in range(n):  # Перевертывание матрицы на 90 градусов
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    rotate_matrix.append(row)

magic_square_check(matrix, summa)  # Вызов функции для проверки является ли матрица магическим квадратом
magic_square_check(rotate_matrix, summa)  # Вызов функции для проверки является ли перевернутая матрица маг. квадратом

print(flag)  # Вывод флага является ли матрица магическим квадратом YES или NO
