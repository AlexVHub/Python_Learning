n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = -999

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            matrix[0][0] = i, j

print(*matrix[0][0])
