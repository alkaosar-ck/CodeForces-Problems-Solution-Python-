for _ in range(int(input())):
   x,n,m = map(int,input().split())
   if x<=10 and m>=1:
      print('YES')
      continue
   elif x<=10 and m<=0:
      print('NO')
      continue
   for _ in range(n):
      x = x//2+10
      if x<=0:
         print('YES')
         break
   x = x-(10*m)
   if x<=0:
      print('YES')
   else:
      print('NO')