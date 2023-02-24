n, m = int(input()), int(input())
mult = [[str(i * j) for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        print(mult[i][j].ljust(3), end='')
    print()