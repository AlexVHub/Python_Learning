n = int(input())
matrix = [input().split() for _ in range(n)]
flag = 'YES'

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = 'NO'
            break

print(flag)