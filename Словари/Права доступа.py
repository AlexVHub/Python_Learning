acl = {'write': 'W', 'read': 'R', 'execute': 'X'}
files = {}

for i in range(int(input())):
    s = input().split()
    files[s[0]] = s[1:]

for j in range(int(input())):
    r = input().split()
    print('OK' if acl[r[0]] in files[r[1]] else 'Access denied')
