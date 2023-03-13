s = input().split()
n = int(input())
list_result = [[] for _ in range(n)]

while len(s) > 0:
    for i in range(n):
        list_result[i].extend(s[:1])
        del s[:1]

print(list_result)
