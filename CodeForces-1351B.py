for _ in range(int(input())):
   a1,b1 = map(int,input().split())
   a2,b2 = map(int,input().split())
   m1 = min(a1,b1)
   m2 = min(a2,b2)
   mx1 = max(a1,b1)
   mx2 = max(a2,b2)
   if (m1+m2 == mx1) and (m1+m2 == mx2):
      print('Yes')
   else:
      print('No')