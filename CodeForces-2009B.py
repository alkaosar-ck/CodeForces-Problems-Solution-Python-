u = []
for _ in range(int(input())):
   n = int(input())
   l = []
   for _ in range(n):
      l.append(input())
   a = []
   for x in l:
      a.append(1 + x.index('#'))
   u.append(reversed(a))
for case in u:
   print(*case)