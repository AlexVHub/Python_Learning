n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]
    continue

for j in matrix:
    print(*j)
