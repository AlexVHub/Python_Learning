mydict = {}

for i in range(int(input())):
    s = input().split()
    mydict[s[0]] = s[1]

s = input()

for key, value in mydict.items():
    if s == key:
        print(value)
        break
    elif s == value:
        print(key)
        break
