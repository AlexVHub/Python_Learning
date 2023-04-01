m, n = int(input()), int(input())
set1 = {input() for _ in range(m)}
set2 = {input() for _ in range(n)}
if len(set1 ^ set2) == 0:
    print('NO')
else:
    print(len((set1 | set2) - (set1 & set2)))
