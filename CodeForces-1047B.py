m = 0
for _ in range(int(input())):
   x,y = map(int,input().split())
   total = x+y
   m = max(m,total)
print(m)