n = input()
s = 0
k = 0
l = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(len(n) - 1, -1, -1):
    if n[i] in l:
        m = l.index(n[i]) + 10
    else:
        m = int(n[i])
    s += m * 16 ** k
    k += 1

print(s)