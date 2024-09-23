i = input().strip().lower()
v = ['a','e','i','o','u','y']
l = list(i)
for x in i:
   if x in v:
      l.remove(x)
j = '.'.join(l)
print(f'.{j}')