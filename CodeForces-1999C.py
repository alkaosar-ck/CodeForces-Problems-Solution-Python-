universal = []
for _ in range(int(input())):
   a,b,c = map(int,input().split())
   u = []
   for _ in range(a):
      l = list(map(int,input().split()))
      u.append(l)
   result = []
   for i in range(a-1):
      result.append(u[i+1][0] - u[i][1])
   result.append(c-u[a-1][1])
   result.append(u[0][0])
   r= max(result)
   if r >= b:
      universal.append('YES')
   else:
      universal.append('NO')
for case in universal:
   print(case)
