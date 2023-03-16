def spiral_filling(n, m, matrix):
    count = 1
    k = 1
    while count < n * m + 1:
        for _ in range(1):
            for i in range(n):
                for j in range(m):
                    if i + j + count == k and matrix[i][j] == 0:
                        matrix[i][j] = count
                        count += 1
                        k += 2
        k -= 2
        for _ in range(1):
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if i + j + count == k and matrix[i][j] == 0:
                        matrix[i][j] = count
                        count += 1
        k += 2


n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

spiral_filling(n, m, matrix)

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
