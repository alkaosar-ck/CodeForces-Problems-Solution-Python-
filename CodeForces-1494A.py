def check_validity(i):
   b = 0
   for x in i:
      if x == '(':
         b+=1
      else:
         b-=1
         if b<0:
            return False
   return b == 0
for _ in range(int(input())):
   import itertools
   i = input().strip()
   chars = 'ABC'
   for map in itertools.product('()', repeat=3):
        bracket_map = dict(zip(chars, map)) 
        b = ''.join(bracket_map[char] for char in i)
        if check_validity(b):
         print('YES')
         break
   else:
      print('NO')
   