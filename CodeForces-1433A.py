for _ in range(int(input())):
   f = 1
   s = 3
   t = 6
   fo = 10
   i = int(input())
   string = str(i)
   le = len(string)
   d = int(string[0])
   total = 10*(d-1)
   if le == f:
      print(total+1)
   if le == 2:
      print(total+s)
   if le == 3:
      print(total+t)
   if le == 4:
      print(total+fo)
   