i = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
n = l1+l3
from collections import Counter
c1 = Counter(l1)
c2 = Counter(l2)
c3 =Counter(l3)
a,b = 0,0
for error in c1:
   if c2[error]!=c1[error]:
      a = error
      break
for error in c2:
   if c3[error]!=c2[error]:
      b = error
      break
print(a)
print(b)
