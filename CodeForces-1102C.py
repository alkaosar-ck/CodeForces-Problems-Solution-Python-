n,x,y = map(int,input().split())
l = list(map(int,input().split()))
import math
if x>y:
   print(n)
else:
   count = sum(1 for i in l if i<=x)
   print(math.ceil(count/2))