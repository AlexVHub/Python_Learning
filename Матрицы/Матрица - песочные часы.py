n = int(input())
matrix = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i > j and i < n - 1 - j or i < j and i > n - 1 - j:
            matrix[i][j] = 0

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
