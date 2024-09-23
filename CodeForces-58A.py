i = input().strip()
l = ['h','e','l','l','o']
start = 0
n = 0
for x in range(len(i)):
   try:
      if i[x] == l[start]:
         n += 1
         start+=1
   except:
      break
if n>=5:
   print('YES')
else:
   print('NO')