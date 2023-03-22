n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

two_book = (n - t + m - x) + (m - t + k - y) + (k - t + n - z)
one_book = n + m + k - two_book * 2 - t * 3
no_book = a - one_book - two_book - t

print(one_book, two_book, no_book, sep='\n')
