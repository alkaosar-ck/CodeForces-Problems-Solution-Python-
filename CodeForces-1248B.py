i = int(input())
L = list(map(int,input().split()))
s = sorted(L)
Rs = s[::-1]
t = i//2
v = 0
a = 0
for x in range(t):
   v+=s[x]
   a+=Rs[x]
if i%2 == 1:
   a+=s[t]
print(a**2+v**2)