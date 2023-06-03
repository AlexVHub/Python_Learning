from random import choice

people = [input() for _ in range(int(input()))]
secret_friends = []

for i in people:
    temp = []
    for j in people:
        if i != j and j not in secret_friends:
            temp.append(j)
    if len(temp) != 0:
        secret_friends.append(choice(temp))
    else:
        secret_friends.append(secret_friends[0])
        secret_friends[0] = i

[print(people[i], '-', secret_friends[i]) for i in range(len(people))]
