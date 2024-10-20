for _ in range(int(input())):
   a,b = map(int,input().split())
   if a>=b:
      print(a)
   else:
      print(max(0,2*a-b))