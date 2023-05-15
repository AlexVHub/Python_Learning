import random

result = []
friends = [input() for _ in range(int(input()))]
count = ((len(friends) - 1) / 2) - 1
for i in friends:
    temp = []
    for j in friends:
        if j not in result and j != i:
            temp.append(j)
    while True:
        choice = random.choice(temp)
        if choice in result:
            if choice == result.index(choice):
                count -= 1
                print(count)
        result.append(choice)
        break

print(result)
