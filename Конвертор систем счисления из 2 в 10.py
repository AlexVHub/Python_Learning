n = int(input())
s = 0
k = 0
while n > 0:
    s += (n % 10) * 2 ** k
    k += 1
    n //= 10
print(s)