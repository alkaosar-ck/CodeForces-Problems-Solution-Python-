for _ in range(int(input())):
   n,k = map(int,input().split())
   L = list(map(int,input().split()))
   m = min(L)
   mx = max(L)
   m = m+k
   mx = mx-k
   if mx<=m:
      print(m)
   else:
      print(-1)