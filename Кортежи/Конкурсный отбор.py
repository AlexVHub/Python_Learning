s = [tuple(input().split()) for _ in range(int(input()))]

[print(*j) for j in s]
print()
[print(*s[k]) for k in range(len(s)) if int(s[k][-1]) > 3]
