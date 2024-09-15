n,m = map(int,input().split())
count = 0
high = round((m+n)**0.5)
target = n+m
for i in range(high+1):
   for j in range(high+1):
      if i*i+j == n:
         if j*j + i == m:
            count+=1
print(count)