queen = input()
chessboard = [['.'] * 8 for _ in range(8)]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

queen_column = letters.index(queen[0])
queen_row = int(queen[1]) - 1

for i in range(8):
    for j in range(8):
        if i == queen_row or j == queen_column or abs(queen_row - i) == abs(j - queen_column):
            chessboard[i][j] = '*'

chessboard[queen_row][queen_column] = 'Q'

[print(*row) for row in chessboard[::-1]]
