n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
c = 1

for i in range(n + m - 1):
    for j in range(n):
        for k in range(m):
            if j + k == i:
                matrix[j][k] = c
                c += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
