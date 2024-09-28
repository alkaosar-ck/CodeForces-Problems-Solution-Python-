for _ in range(int(input())):
   i = int(input())
   L = list(map(int,input().split()))
   m = max(L)
   c = L.copy()
   c.remove(m)
   m1 = max(c)
   idx = L.index(m)
   new = []
   for x in range(i):
      if x != idx:
         new.append(L[x]-m)
      else:
         new.append(m-m1)
   print(*new)