n, m = input().split()
matrix = []
k = 1

for _ in range(int(n)):
    row = []
    for _ in range(int(m)):
        row.append(str(k).ljust(3))
        k += 1
    matrix.append(row)

for row in matrix:
    print(*row)
