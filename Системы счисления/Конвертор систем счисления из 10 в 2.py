n = int(input())
m = ''

while n > 0:
    s = n % 2
    m += str(s)
    n //= 2

print(m[::-1])