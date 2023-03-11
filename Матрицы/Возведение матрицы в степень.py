def matrix_exponent(n, matrix, matrix_result):
    matrix_temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_temp[i][j] += matrix_result[i][k] * matrix[k][j]
    return matrix_temp


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
matrix_result = matrix.copy()

for _ in range(m - 1):
    matrix_result = matrix_exponent(n, matrix, matrix_result)

for row in matrix_result:
    print(*row)
