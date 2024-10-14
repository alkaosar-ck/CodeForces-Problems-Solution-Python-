i = int(input())
L = list(map(int,input().split()))
s = sorted(L)
s = s[::-1]
x = 1
total = 1
start = 0
for i in s[1:]:
   total+=(i*x+1)
   x+=1
print(total)
lens = []
for x in s:
   i = L.index(x)
   lens.append(i+1)
   L[i] = -1
print(*lens)