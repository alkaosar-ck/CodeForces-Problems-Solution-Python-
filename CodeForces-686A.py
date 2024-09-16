n,x = map(int,input().split())
l = [input() for _ in range(n)]
remain = x
distressed = 0
for j in l:
   if j[0] == '+':
      remain+=int(j[2:])
   else:
      if remain<int(j[2:]):
         remain = remain
         distressed+=1
      else:
         remain-=int(j[2:])
print(remain,distressed)
