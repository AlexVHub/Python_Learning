n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
s = input()
i, j = int(s[0]), int(s[2])

for k in range(n):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
    print(*matrix[k])
