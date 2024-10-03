
def check(a,b,r):
   if b in a :
      return 0
   else:
      for x in range(r):
         a+=a
         if b in a:
            return x+1
      return -1
for _ in range(int(input())):
   i,j = map(int,input().split())
   a = input().strip()
   b = input().strip()
   import math
   if j>i:
      r = int(math.log2(j))+1
   else:
      r = 10
   print(check(a,b,r))
   