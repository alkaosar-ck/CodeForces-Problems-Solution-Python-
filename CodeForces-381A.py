n = int(input())
l = list(map(int,input().split()))
s = 0
d = 0
i = len(l)
if i%2 != 0:
   for _ in range(len(l)//2):
      first_max = max(l[0],l[-1])
      s+=first_max
      l.remove(first_max)
      second_max = max(l[0],l[-1])
      d+=second_max
      l.remove(second_max)
   s+=l[0]
else:
   for _ in range(len(l)//2):
      first_max = max(l[0],l[-1])
      s+=first_max
      l.remove(first_max)
      second_max = max(l[0],l[-1])
      d+=second_max
      l.remove(second_max)
print(s,d)