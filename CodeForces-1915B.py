t = int(input())
for _ in range(t):
   a = input().strip()
   b = input().strip()
   c = input().strip()
   for x in range(3):
      if a[x] == '?':
         if 'A' in a and 'B' in a:
            print('C')
            break
         if 'B' in a and 'C' in a:
            print('A')
            break
         if 'A' in a and 'C' in a:
            print('B')
            break
      if b[x] == '?':
         if 'A' in b and 'B' in b:
            print('C')
            break
         if 'B' in b and 'C' in b:
            print('A')
            break
         if 'A' in b and 'C' in b:
            print('B')
            break
      if c[x] == '?':
         if 'A' in c and 'B' in c:
            print('C')
            break
         if 'B' in c and 'C' in c:
            print('A')
            break
         if 'A' in c and 'C' in c:
            print('B')
            break
         