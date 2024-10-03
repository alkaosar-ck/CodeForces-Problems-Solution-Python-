n,m = map(int,input().split())
turned_on = set()
for _ in range(n):
   inputs = list(map(int,input().split()))
   f = inputs[0]
   buttons = inputs[1:]
   turned_on.update(buttons)
if len(turned_on) == m:
   print('YES')
else:
   print('NO')