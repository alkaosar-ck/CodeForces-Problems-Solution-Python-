
for _ in range(int(input())):
   i = int(input())
   s = input().strip()
   found = False
   x,y = 0,0
   for k in s:
      if k == 'L':
         x-=1
      elif k == 'R':
         x+=1
      elif k == 'U':
         y+=1
      elif k == 'D':
         y-=1
      if x==1 and y == 1:
         found = True
   if found:
      print('YES')
   else:
      print('NO')