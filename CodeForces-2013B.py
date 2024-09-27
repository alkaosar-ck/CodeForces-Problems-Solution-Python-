for _ in range(int(input())):
   n = int(input())
   l = list(map(int,input().split()))
   s = sum(l)
   print(s-2*l[n-2])

   
   