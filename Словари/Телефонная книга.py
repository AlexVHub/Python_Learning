phone_book = {}

for i in range(int(input())):
    phone, name = input().lower().split()
    phone_book[name] = phone_book.get(name, '') + phone + ' '

[print(phone_book.get(input().lower(), 'абонент не найден').strip()) for _ in range(int(input()))]
