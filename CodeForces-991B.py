i = int(input())
L =list(map(int,input().split()))
s = sum(L)
total = 0
avarage = s/i
if avarage>=4.5:
   print(0)
else:
   m = min(L)
   L.remove(m)
   L.append(5)
   total = 1
   s = sum(L)/i
   while s<4.5:
      m = min(L)
      L.remove(m)
      L.append(5)
      s = sum(L)/i
      total+=1
   print(total)