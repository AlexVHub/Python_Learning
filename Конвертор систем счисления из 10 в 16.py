n = int(input())

l = ['A', 'B', 'C', 'D', 'E', 'F']
m = ''

while n > 16:
    s = n % 16
    if s > 9:
        m += str(l[s - 10])
    else:
        m += str(s)
    n = n // 16
m += str(n)

print(m[::-1])