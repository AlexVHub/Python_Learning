n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = -999
k = 0

for i in range(n):
    if k + i < n:
        k += 1
    elif k + i > n:
        k -= 1
    maximum = max(max(matrix[i][:k]), max(matrix[i][-k:]), maximum)

print(maximum)