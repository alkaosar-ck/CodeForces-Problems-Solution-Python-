n = input().strip()
if n == '{}':
   print(0)
else:
   n = n[1:-1]
   n = n.split(', ')
   s = set(n) if n!= [''] else set()
   print(len(s))
