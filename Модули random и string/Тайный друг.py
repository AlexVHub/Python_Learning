import random

result = dict()
friends = [input() for _ in range(int(input()))]
count = int(len(friends) / 2)

for i in friends:
    temp = []
    for j in friends:
        if i != j and j not in result.values():
            temp.append(j)
    print(temp)
    print(result)
    while True:
        choice = random.choice(temp)
        if choice in result.values():
            continue
        else:
            result.setdefault(i, choice)
            break


print(result)
