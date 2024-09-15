def head(m):
   print('#'*m)
def dot(n,pos):
   if pos == 'right':
      print('.'*(n-1) + '#')
   else:
      print('#'+(n-1)*'.')

def pattern(n,m):
   for x in range(n):
      if x%2 == 0:
         head(m)
      else:
         if (x//2)%2 == 0:
            dot(m,'right')
         else:
            dot(m,'left')
n,m = map(int,input().split())
pattern(n,m)