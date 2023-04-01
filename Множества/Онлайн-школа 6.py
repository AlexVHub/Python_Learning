m = int(input())
set1 = {input() for _ in range(int(input()))}

for i in range(m - 1):
    n = int(input())
    set2 = {input() for _ in range(n)}
    set1.intersection_update(set2)

print(*sorted(set1))
