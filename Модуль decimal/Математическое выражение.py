from decimal import *

num = Decimal('12.1244354689')

s = [i for i in str(num) if i.isdigit()]
print(int(min(s)) + int(max(s)))
