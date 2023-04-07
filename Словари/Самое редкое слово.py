s = [i.strip('.,!?:;-').lower() for i in input().split()]
result = {}

for i in s:
    result[i] = result.get(i, 0) + 1

print(min([key for key, value in result.items() if value == min(result.values())]))
