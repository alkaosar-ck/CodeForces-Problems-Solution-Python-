d = set()
d.add(0)
current = 0
i = int(input())
l = list(map(int,input().split()))
total = 0
for x in range(i):
    current +=l[x]
    if current in d:
        total+=1
        current = l[x]
        d = set()
        d.add(0)
    d.add(current)
print(total)