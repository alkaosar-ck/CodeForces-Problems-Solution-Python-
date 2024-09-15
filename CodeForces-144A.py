
n = int(input())
l = list(map(int, input().split())) 

mi = min(l)
mx = max(l)

amax = l.index(mx)

amin = len(l) - 1 - l[::-1].index(mi)

n1 = amax

n2 = (n - amin - 1)

if amax > amin:
    print(n1 + n2 - 1)
else:
    print(n1 + n2)
