def pascal(n):
    l = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = l[i - 1][j - 1] + l[i - 1][j]
        l.append(row)
    return l[-1]


print(pascal(int(input())))