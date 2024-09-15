n = input()
r = len(n) 
o = []
x = 0
while x<r:
   if n[x] == '.':
      o.append('0')
      x+=1
   elif n[x] == '-' and x+1<r:
      if n[x+1] == '.':
         o.append('1')
      elif n[x+1] == '-':
         o.append('2')
      x+=2
   else:
      x+=1
for x in o:
   print(''.join(x),end='')