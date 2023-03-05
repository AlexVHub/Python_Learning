n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
count = 1
row = 0
col = 0

for i in range(20):
    print(row, col, i)
    if col < 0:
        col = row
    if i == 1:
        row = 0
    print(row, col, i)
    if col > (m - 1):
        col -= 2
        row += 1
    print(row, col, i)
    matrix[row][col] = count
    print(matrix)
    count += 1
    col -= 1
    row += 1
    if row > n - 1:
        row = 0


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
