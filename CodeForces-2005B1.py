for _ in range(int(input())):
   n,m,q = map(int,input().split())
   t1,t2 = map(int,input().split())
   s = int(input())
   f1,f2 = sorted([t1,t2])
   if s<=f1:
      print(f1-1)
   elif s>=f2:
      print(n-f2)
   else:
      print((f2-f1)//2)