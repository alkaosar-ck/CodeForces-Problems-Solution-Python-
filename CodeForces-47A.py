n = int(input())
is_tri = False
for k in range(1,10000):
   t_k = k*(k+1)//2
   if t_k == n:
      is_tri = True
      break
   if t_k>n:
      break
if is_tri:
   print('YES')
else:
   print('NO')