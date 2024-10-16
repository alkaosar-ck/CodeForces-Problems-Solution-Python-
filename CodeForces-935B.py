x,y = 0,0
points = []
i = int(input())
s = input().strip()
for k in s:
   if k == 'U':
      y+=1
   if k == 'R':
      x+=1
   points.append((x,y))
total = 0
for x in range(len(points)-1):
   try:
      px,py = points[x-1]
      fx,fy = points[x]
      sx,sy = points[x+1]
      if fx == fy:
         if px == fx == sx and py+2 == fy+1 == sy:
            total+=1
         elif py == fy == sy and px+2 == fx+1 == sx:
            total+=1
   except:
      pass
print(total)