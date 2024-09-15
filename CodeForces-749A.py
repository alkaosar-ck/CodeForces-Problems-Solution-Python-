n = int(input())
if n%2 == 0:
   t = n//2
   print(t)
   print('2 '*t)
else:
   t = n//2-1
   print(t+1)
   print('2 '*t+'3')