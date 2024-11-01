i = (input())
l = list(i)
if '0' in l:
   l.remove('0')
   print(''.join(l))
else:
   l.reverse()
   l.remove('1')
   l.reverse()
   print(''.join(l))