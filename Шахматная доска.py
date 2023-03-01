n, m = 3, 4
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2:
            s = '*'
        else:
            s = '.'
        row.append(s)
    matrix.append(row)

for r in matrix:
    print(*r)
