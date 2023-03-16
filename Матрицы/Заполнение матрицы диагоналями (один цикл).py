n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
row = 0
col = 0
count = 1

for i in range(n * m):
    matrix[row][col] = count
    count += 1
    row += 1
    col -= 1
    if col < 0 or (col >= 0 and row == n):
        if row + col + 1 < m:
            col = row + col + 1
            row = 0
        else:
            row, col = row + col + 1 - (m - 1), m - 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
