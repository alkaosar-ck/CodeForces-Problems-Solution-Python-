i = int(input())
l = list(map(int,input().split()))
total = 0
for i in range(1,i-1):
   if l[i-1] == 1 and l[i] == 0 and l[i+1] == 1:
      total+=1
      l[i+1] = 0
print(total)