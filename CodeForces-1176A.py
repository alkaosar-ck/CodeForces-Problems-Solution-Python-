def calculate(i):
   count = 0
   while i!=1:
      if i%2 == 0:
         count+=1
         i = (i//2)
      elif i%3 == 0:
         count+=1
         i = (2*i)//3
      elif i%5 == 0:
         count+=1
         i = (4*i)//5
      else:
         return -1
   return count
      
for _ in range(int(input())):
   i = int(input())
   if i == 1:
      print(0)
      continue
   else:
      print(calculate(i))