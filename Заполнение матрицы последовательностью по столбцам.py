n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
c = 1

for i in range(m):
    for j in range(n):
        matrix[j][i] = c
        c += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
