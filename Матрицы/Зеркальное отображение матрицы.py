n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

for row in matrix:
    print(*row)
