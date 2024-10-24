import math
for _ in range(int(input())):
   i = int(input())
   l = sorted(list(map(int,input().split())))
   o = len(l)
   l.sort(key=lambda x: x % 2)
   total = 0
   for x in range(o):
      for i in range(x+1,o):
         if math.gcd(l[i]*2,l[x])>1:
            total+=1
   print(total)