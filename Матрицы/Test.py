n, m = 3, 6
matrix = [[0] * m for _ in range(n)]
count = 1
row = 0
col = 0
temp = 0
flag = False

while count < 13:
    matrix[row][col] = count
    count += 1
    if flag == False:
        col += 1
        flag = True
        continue
    col -= 1
    row += 1
    if col < 0 or row > n - 1:
        temp = col
#        if row == n:
#            row -= 1
#            temp += 1
        col = row
        row = temp + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
