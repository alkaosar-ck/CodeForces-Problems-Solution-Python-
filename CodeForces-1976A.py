def validity(n,l):
   digits = []
   char = []
   for x in l:
      if x.isdigit():
         digits.append(x)
      else:
         char.append(x)
   if digits != sorted(digits):
      return 'NO'
   if char != sorted(char):
      return 'NO'
   if len(char)>0 and len(digits)>0:
      first_char = l.index(char[0])
      last_digit = l.index(digits[-1])
      if last_digit>first_char:
         return 'NO'
   return 'YES'
for _ in range(int(input())):
   n = int(input())
   l = list(input().strip())
   print(validity(n,l))
  
