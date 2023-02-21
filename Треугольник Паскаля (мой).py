def pascal(n):
    l = [[]]
    for i in range(n + 1):
        l.append([1])
        for j in range(1, i):
            elem = l[i - 1][j] + l[i - 1][j - 1]
            l[i].append(elem)
        l[i].append(1)
    return l[-2]


print(pascal(int(input())))