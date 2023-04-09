countries = {}

for i in range(int(input())):
    s = input().split()
    countries[s[0]] = s[1:]

for j in range(int(input())):
    t = input()
    for key, value in countries.items():
        if t == value:
            print(key)
            continue
