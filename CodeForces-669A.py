n = int(input())
if n == 1 or n == 2:
   print(1)
else:
   if n%2 == 0 and n%3 == 0:
      print((n//3)*2)
   elif n%2 == 0 and n%3!=0:
      print((n//3)*2+1)
   if n%2 == 1 and n%3 == 0:
      print((n//3)*2)
   elif n%2 == 1 and n%3!=0:
      print((n//3)*2+1)