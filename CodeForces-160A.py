n = int(input())
l = list(map(int,input().split()))
l.sort()
if n == 1:
   print(1)
elif n>=2:
   my_coin = 0
   remaining = 0
   x = 0
   s = sum(l)
   while True:
      my_coin+=max(l)
      x+=1
      l.remove(max(l))
      remaining = s-my_coin
      if my_coin>remaining:
         print(x)
         break
