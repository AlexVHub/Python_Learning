set1, set2 = [set(int(i) for i in input().split()) for _ in range(2)]
print(*sorted(set1 - set2))
