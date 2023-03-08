n, m = 3, 4
matrix = [[0] * m for _ in range(n)]
count = 1
row = 0
col = 0
k = 0

for i in range(5):
    while row < n and col >= 0:
        matrix[row][col] = count
        count += 1
        if col <= 0:
            row, col = col, row
            col += 1
            break
        else:
            row += 1
            col -= 1


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
