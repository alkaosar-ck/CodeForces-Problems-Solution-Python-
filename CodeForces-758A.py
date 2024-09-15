n = int(input())
l = list(map(int,input().split()))
if n == 1:
   print(0)
else:
   m = max(l)
   s = sum(l)
   need = m*n
   print(need-s)