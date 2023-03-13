n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

[print(*row) for row in matrix]
