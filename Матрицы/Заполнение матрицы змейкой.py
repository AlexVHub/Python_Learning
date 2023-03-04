n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
c = 0

for i in range(n):
    for j in range(m):
        c += 1
        if i % 2:
            matrix[i][-j - 1] = c
        else:
            matrix[i][j] = c

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
