m, n = int(input()), int(input())
set1 = {input() for _ in range(m + n)}
result = len(set1) * 2 - m - n
print('NO' if result == 0 else result)
