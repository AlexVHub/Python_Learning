s = [int(i) for i in input().split()]
set1 = set()
for i in s:
    if i in set1:
        print('YES')
    else:
        print('NO')
        set1.add(i)
