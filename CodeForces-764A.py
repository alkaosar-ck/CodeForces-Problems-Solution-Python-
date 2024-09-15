a,b,n = map(int,input().split())
import math
r1 = math.floor(n/a)
r2 = math.floor(n/b)
l1 = [a*x for x in range(1,r1+1)]
l2 = [b*x for x in range(1,r2+1)]
s = sum(1 for i in l1 if i in l2)
print(s)