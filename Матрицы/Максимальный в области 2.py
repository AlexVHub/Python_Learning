n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = -999

for i in range(n):
    for j in range(n):
        if i >= n - j - 1 and matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)
