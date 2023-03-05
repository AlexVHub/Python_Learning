n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        print('[', i, ']', '[', j, ']', sep = '', end = '  ')
    print()