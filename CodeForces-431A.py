a,b,c,d = map(int,input().split())
s = input().strip()

from collections import Counter

C = Counter(s)

total = a * C['1'] + b * C['2'] + c * C['3'] + d * C['4']
print(total)