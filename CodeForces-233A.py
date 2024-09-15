n = int(input())
u = []
if n%2 == 1:
   print(-1)
else:
   for x in range(n):
      if x %2 == 0:
         u.append(x+2)
      else:
         u.append(x)
print(*u)