for _ in range(int(input())):
   n = int(input())
   l = list(map(int,input().split()))
   f = list(set(l))
   a,b = f[0],f[1]
   if l.count(a) == 1:
      print(l.index(a)+1)
   else:
      print(l.index(b)+1)
   