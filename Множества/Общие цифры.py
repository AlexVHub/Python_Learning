n = int(input())
set1 = set(input())
[set1.intersection_update(set(input())) for _ in range(n - 1)]
print(*sorted(set1))
