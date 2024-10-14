i = int(input())
L = list(map(int,input().split()))
c = L.copy()
for x in c:
   L.append(x)
h = 1
m = 1
if all(x == 0 for x in L):
   print(0)
else:
   for x in range(len(L)-1):
      if L[x] == 1 and L[x+1] == 1:
         h+=1
         m = max(m,h)
      else: 
         h = 1
   print(m)
