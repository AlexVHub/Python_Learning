def latin_square(n, matrix, list_search, flag):
    for k in list_search:
        for i in range(n):
            print(k, i)
            if k not in matrix[i]:
                flag = 'NO'
                break
    return flag


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = 'YES'
list_search = [int(i) for i in range(1, n + 1)]

flag = latin_square(n, matrix, list_search, flag)

for i in range(n):
    for j in range(n):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

flag = latin_square(n, matrix, list_search, flag)

print(flag)
