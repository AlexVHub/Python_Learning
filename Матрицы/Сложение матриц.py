n, m = [int(i) for i in input().split()]
matrix_a = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrix_b = [[int(i) for i in input().split()] for _ in range(n)]
matrix_result = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix_result[i][j] = matrix_a[i][j] + matrix_b[i][j]

for row in matrix_result:
    print(*row)
