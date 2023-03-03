row = int(input())
column = int(input())
matrix = []
count = 0

for r in range(row):
    matrix.append([])
    for c in range(column):
        matrix[r].append(input())

while count < 2:
    for r in range(row):
        for c in range(column):
            if count == 0:
                print(matrix[r][c], end=' ')
            else:
                print(matrix[c][r], end=' ')
        print()
    print()
    count += 1
    row, column = column, row
