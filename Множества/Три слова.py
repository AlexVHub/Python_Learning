s = input().split()
flag = 'YES'

for i in s:
    if set(s[0]) != set(i):
        flag = 'NO'
        break

print(flag)
