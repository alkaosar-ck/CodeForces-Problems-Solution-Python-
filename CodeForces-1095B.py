i = int(input())
L = list(map(int,input().split()))
if i == 2:
   print(0)
else:
   m1 = max(L)
   mi1 = min(L)
   L.remove(m1)
   m2 = max(L)
   L.remove(mi1)
   mi2 = min(L)
   print(min((m1-mi2),(m2-mi1)))