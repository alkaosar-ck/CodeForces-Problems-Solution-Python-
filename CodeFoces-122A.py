def lucky(i):
   i = str(i)
   for x in i:
      if x != '4' and x != '7': 
         return False
   return True

lucky_numbers = []
for x in range(1, 1001):
   if lucky(x):
      lucky_numbers.append(x)

n = int(input())

almost_lucky = False
for lucky_num in lucky_numbers:
   if n % lucky_num == 0:
      almost_lucky = True
      break
if almost_lucky:
   print('YES')
else:
   print('NO')
