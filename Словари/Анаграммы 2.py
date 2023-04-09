mydict = {}

for i in range(2):
    mydict[i] = sorted([s for s in input().lower() if s not in '., !?:;-'])

if mydict[0] == mydict[1]:
    print('YES')
else:
    print('NO')
