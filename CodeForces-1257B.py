def calculate(x,y):
   if x >= y:
      return 'YES'
   if x == 1 and y!=1:
      return 'NO'
   if (x == 2 or x == 3) and y>3:
      return "NO"
   else:
      return "YES"



for _ in range(int(input())):
   x,y = map(int,input().split())
   print(calculate(x,y))