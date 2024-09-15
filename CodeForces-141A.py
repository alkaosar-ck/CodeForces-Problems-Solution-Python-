a = input()
b = input()
c = input()
from collections import Counter

a = Counter(a)
b = Counter(b)
l = Counter(a)+Counter(b)
c = Counter(c)
if l == c:
   print('YES')
else:
   print('NO')