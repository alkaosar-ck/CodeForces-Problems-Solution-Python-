n, k =map(int,input().split())
l = input()
G = l.index('G')
T = l.index("T")
if G<T:
   i = G+k
   while i<=T:
      if l[i] == '#':
         print('NO')
         break

      elif l[i] == 'T':
         print('YES')
         break
      i+=k
   else:
      print('NO')
else:
   i = G-k
   while i>=T:
      if l[i] == '#':
         print('NO')
         break
      elif l[i] == 'T':
         print('YES')
         break
      i-=k
   else:
      print('NO')
   
   
         

      