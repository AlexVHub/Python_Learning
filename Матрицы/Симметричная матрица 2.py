n = int(input())
matrix = [input().split() for _ in range(n)]
flag = 'YES'

for i in range(n):
    for j in range(n):
        if (i == j or i < n - 1 - j) and matrix[i][j] != matrix[-j + n - 1][-i + n - 1]:
            flag = 'NO'
            break

print(flag)