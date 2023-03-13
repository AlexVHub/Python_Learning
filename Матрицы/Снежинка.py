n = int(input())
matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - 1 - j or i == (n - 1) // 2 or j == (n - 1) // 2:
            matrix[i][j] = '*'

[print(*row) for row in matrix]
