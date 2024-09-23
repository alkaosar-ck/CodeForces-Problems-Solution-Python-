for _ in range(int(input())):
   i = int(input())
   l = list(map(int,input().split()))
   s = sum(l)
   sq = s**0.5
   if sq > int(sq):
      print('NO')
   else:
      print('YES')