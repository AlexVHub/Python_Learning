n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
top = 0
right = 0
down = 0
left = 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            top += matrix[i][j]
        if i < j and i > n - 1 - j:
            right += matrix[i][j]
        if i > j and i > n - 1 - j:
            down += matrix[i][j]
        if i > j and i < n - 1 - j:
            left += matrix[i][j]

print('Верхняя четверть:', top)
print('Правая четверть:', right)
print('Нижняя четверть:', down)
print('Левая четверть:', left)
