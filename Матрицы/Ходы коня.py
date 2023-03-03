knight = input()
chessboard = [['.'] * 8 for i in range(8)]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

knight_column = letters.index(knight[0])
knight_row = int(knight[1]) - 1
chessboard[knight_row][knight_column] = 'N'

for i in range(8):
    for j in range(8):
        if (i - knight_row) ** 2 + (j - knight_column) ** 2 == 5:
            chessboard[i][j] = '*'

for r in chessboard[::-1]:
    print(*r)
