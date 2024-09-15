n = input().lower()
l = n.split()
vowel = ['a','e','i','o','u','y']
n = l[-1]
if n == '?':
   n =l[-2]
   if n[-1] in vowel:
      print('YES')
   else:
      print('NO')
else:
   n = l[-1]
   if n[-2] in vowel:
      print('YES')
   else:
      print('NO')