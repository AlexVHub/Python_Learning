mydict = {}
for i in input().split():
    mydict[i] = mydict.get(i, 0) + 1
    print(mydict[i], end=' ')
