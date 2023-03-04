def print_go_buhat(s, f):
    n, le = 10, 75
    li = [[f] * le for _ in range(n)]
    li[3][3], li[3][4], li[3][5], li[3][6], li[3][7] = s, s, s, s, s
    li[4][3], li[5][3], li[6][3], li[7][3], li[8][3] = s, s, s, s, s
    li[3][11], li[3][12], li[3][13], li[3][14], li[3][15] = s, s, s, s, s
    li[4][11], li[5][11], li[6][11], li[7][11], li[8][11] = s, s, s, s, s
    li[8][12], li[8][13], li[8][14], li[8][15] = s, s, s, s
    li[4][15], li[5][15], li[6][15], li[7][15], = s, s, s, s
    #  Б
    li[3][19], li[3][20], li[3][21], li[3][22], li[3][23] = s, s, s, s, s
    li[4][19], li[5][19], li[6][19], li[7][19], li[8][19] = s, s, s, s, s
    li[8][20], li[8][21], li[8][22], li[8][23] = s, s, s, s
    li[7][23], li[6][23], li[5][23] = s, s, s
    li[5][22], li[5][21], li[5][20] = s, s, s
    #  У
    li[3][27], li[4][28], li[5][29], li[6][30] = s, s, s, s
    li[3][31], li[4][31], li[5][31] = s, s, s
    li[7][29], li[8][28] = s, s
    #  Х
    li[3][35], li[4][36], li[5][37], li[6][38], li[7][39], li[8][40] = s, s, s, s, s, s
    li[8][35], li[7][36], li[6][37], li[5][38], li[4][39], li[3][40] = s, s, s, s, s, s
    #  А
    li[8][44], li[7][45], li[6][46], li[5][47], li[4][48], li[3][49], = s, s, s, s, s, s
    li[4][50], li[5][51], li[6][52], li[7][53], li[8][54] = s, s, s, s, s
    li[6][47], li[6][48], li[6][49], li[6][50], li[6][51] = s, s, s, s, s
    #  T
    li[3][58], li[3][59], li[3][60], li[3][61], li[3][62], li[3][63], li[3][64] = s, s, s, s, s, s, s
    li[4][61], li[5][61], li[6][61], li[7][61], li[8][61] = s, s, s, s, s
    # b
    li[3][68], li[4][68], li[5][68], li[6][68], li[7][68], li[8][68] = s, s, s, s, s, s
    li[8][69], li[8][70], li[8][71], li[8][72] = s, s, s, s
    li[7][72], li[6][72], li[5][72] = s, s, s
    li[5][71], li[5][70], li[5][69] = s, s, s

    for row in range(n):
        for cols in range(le):
            print(li[row][cols], end=' ')
        print()


sumbol, fon = '''qwertyuiopasdfghjklzxcvbnm''', '''!@#$%^&*()_-=+;:<.,>1234567890'''

while True:
    for i in fon:
        for j in sumbol:
            print_go_buhat(j, i)
