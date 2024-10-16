import math
for _ in range(int(input())):
   n,x = map(int,input().split())
   L = (list(map(int,input().split())))
   total = sum(L)
   f = math.ceil(total/x)
   f2 = max(L)
   print(max(f,f2))
