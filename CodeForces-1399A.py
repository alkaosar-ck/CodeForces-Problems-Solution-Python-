for _ in range(int(input())):
   n= int(input())
   l = list(map(int,input().split()))
   u = []
   l = sorted(l)
   if n ==1:
      print('YES')
   else:
      for x in range(n-1,0,-1):
         u.append(abs(l[x]-l[x-1]))
      l = [True for x in u if x<=1]
      if len(u) == len(l):
         print('YES')
      else:
         print("NO")