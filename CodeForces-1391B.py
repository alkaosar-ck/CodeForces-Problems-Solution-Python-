for _ in range(int(input())):
   n,m = map(int,input().split())
   L = [input().strip() for _ in range(n)]
   u = []
   r = L[n-1]
   for x in L:
      u.append(x[-1])
   u = u.count('R')
   r = r.count('D')
   print(u+r)