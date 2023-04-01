m, n = int(input()), int(input())
set1 = {input() for _ in range(m)}
set2 = {input() for _ in range(n)}

print(len(set1 - set2))
