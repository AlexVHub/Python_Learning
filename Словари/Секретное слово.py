mydict = {}
s = input()

for i in range(int(input())):
    f = input()
    mydict[int(f[3:])] = f[0]

for j in s:
    s = s.replace(j, mydict.pop(s.count(j), j))

print(s)
