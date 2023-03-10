n, m = [int(i) for i in input().split()]
matrix_a = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrix_b = [[int(i) for i in input().split()] for _ in range(m)]
matrix_result = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for s in range(m):
            matrix_result[j][i] += matrix_a[j][s] * matrix_b[s][i]

for row in matrix_result:
    print(*row)
