s = input().split()
result = {}

for i in s:
    print(*((i, '_', result[i]) if i in result else i), sep='', end=' ')
    result[i] = result.get(i, 0) + 1
