answer = 0
a,b = map(int,input().split())
l = list(map(int,input().split()))
start = 0
for i in l:
   start+=1
   for j in range(start,a):
      if abs(i-l[j])<=b:
         answer += 1
print(answer*2)