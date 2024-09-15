import sys
n = input().strip()
n = list(n)
n = len(set(n))
if n%2 == 0:
   print('CHAT WITH HER!')
else:
   print('IGNORE HIM!')
