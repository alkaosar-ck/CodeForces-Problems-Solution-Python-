n,c = map(int,input().split())
remain = 1
list = list(map(int,input().split()))
for i in range(1,n):
   if list[i] - list[i-1]>c:
      remain = 1
   else:
      remain+=1
print(remain)
      