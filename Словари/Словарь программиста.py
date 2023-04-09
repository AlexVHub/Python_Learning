n = int(input())
dictionary = {}

for i in range(n):
    s = input().replace(':', '').split()
    dictionary[s[0].lower()] = ' '.join(s[1:])

[print(dictionary.get(input().lower(), 'Не найдено')) for _ in range(int(input()))]
