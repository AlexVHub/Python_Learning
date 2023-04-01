m, n = int(input()), int(input()),
home_books = {input() for _ in range(m)}
read_books = [input() for _ in range(n)]

for book in read_books:
    if book in home_books:
        print('YES')
    else:
        print('NO')
