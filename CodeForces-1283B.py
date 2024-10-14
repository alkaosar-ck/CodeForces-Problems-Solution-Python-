for _ in range(int(input())):
   n,k = map(int,input().split())
   total = 0
   r = n//k
   total = k*r
   l = min(n%k,k//2)
   total+=l
   print(total)