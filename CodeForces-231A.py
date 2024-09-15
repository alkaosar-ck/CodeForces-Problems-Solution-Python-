count = 0
for _ in range(int(input())):
   u = list(map(int,input().split()))
   s = sum(u)
   if s>=2:
      count+=1
print(count)