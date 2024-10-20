i = int(input())
l = list(map(int, input().split()))
index_max = l.index(max(l))
possible = True
for x in range(0, index_max):
    possible &= (l[x] < l[x + 1])
for x in range(index_max, i - 1):
    possible &= (l[x] > l[x + 1])

if possible:
    print('YES')
else:
    print('NO')
