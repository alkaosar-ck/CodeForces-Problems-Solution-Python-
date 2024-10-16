for _ in range(int(input())):
   i = int(input())
   L = sorted(list(map(int,input().split())))
   highest = 0
   possible = False
   for x in range(i-1,-1,-1):
      if L[x]<=x+1:
         print(x+2)
         possible =True
         break
   if not possible:
      print(1)
   