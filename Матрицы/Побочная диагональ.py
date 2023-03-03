n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][-i - 1] = 1
    for j in range(i):
        matrix[i][-j - 1] = 2

for row in matrix:
    print(*matrix)
