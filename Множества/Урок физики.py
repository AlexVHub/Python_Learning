set1, set2, set3 = [set(int(i) for i in input().split()) for _ in range(3)]
print(*sorted(set3 - (set1 | set2), reverse=True))
