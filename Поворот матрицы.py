n = int(input())
matrix = [input().split() for _ in range(n)]
rotate_matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    rotate_matrix.append(row[::-1])

for r in rotate_matrix:
    print(*r)
