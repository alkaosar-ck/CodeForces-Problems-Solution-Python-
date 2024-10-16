x = input().strip()
y = input().strip()
possible = True
z = ''
for i in range(len(x)):
   if ord(x[i])<ord(y[i]):
      possible = False
   elif ord(x[i]) == ord(y[i]):
      z+='z'
   else:
      z+=chr(min(ord(x[i]),ord(y[i])))
if possible:
   print(z)
else:
   print(-1)