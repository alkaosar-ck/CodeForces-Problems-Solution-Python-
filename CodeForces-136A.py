n = int(input())
l = list(map(int,input().split()))
index = []
for i,x in enumerate(l,start=1):
  index.append(l.index(i)+1)
print(*index)