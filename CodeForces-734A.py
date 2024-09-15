n = int(input())
l = input().strip()
from collections import Counter
d = l.count('D')
a = l.count('A')
if d>a:
    print('Danik')
elif d<a:
    print('Anton')
else:
    print('Friendship')