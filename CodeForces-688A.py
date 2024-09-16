n,d = map(int,input().split())
days = [input() for _ in range(d)]
sa = []
for i in days:
   s = 0
   s = sum(int(j) for j in i)
   sa.append(s)
ne= [s<n for s in sa]

cons = []
mx = 0
current  = 0
for x in ne:
   if x :
      current+=1
      mx = max(mx,current)
   else:
      current = 0
   cons.append(max)
print(mx)
      
   