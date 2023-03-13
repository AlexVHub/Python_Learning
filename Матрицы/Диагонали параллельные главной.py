n = int(input())
[print(*[abs(i - j) for j in range(n)]) for i in range(n)]
