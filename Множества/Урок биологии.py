set1, set2, set3 = [set(int(i) for i in input().split()) for _ in range(3)]
print(*[i for i in range(11) if i not in set1 | set2 | set3])
