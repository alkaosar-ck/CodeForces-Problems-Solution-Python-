i = int(input())
l = list(map(int,input().split()))
for x in l:
   m = x%14
   d = x//14
   if d>0 and m>=1 and m<=6:
      print('YES')
   else:
      print('NO')