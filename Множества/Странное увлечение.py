set1, set2 = [{int(i) for i in input().split()} for _ in range(2)]
if set1.isdisjoint(set2):
    print('BAD DAY')
else:
    print(*sorted(set1 & set2, reverse=True))
