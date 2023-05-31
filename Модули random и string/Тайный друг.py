import random

people = [input() for _ in range(int(input()))]
secret_friends = people.copy()
flag = False

while not flag:
    random.shuffle(secret_friends)
    flag = True
    for i in range(len(people)):
        if people[i] == secret_friends[i]:
            flag = False
            break

[print(people[i], '-', secret_friends[i]) for i in range(len(people))]
