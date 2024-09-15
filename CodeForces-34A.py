l = []
n = int(input())
h = list(map(int,input().split()))
for x in range(n-1):
   l.append(abs(h[x+1]-h[x]))
l.append(abs(h[0]-h[n-1]))
mi = min(l)
mi = l.index(mi)
if mi == n-1:
   print(len(l),1)
else:
   print(mi+1,mi+2)