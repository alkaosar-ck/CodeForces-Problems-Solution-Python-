a,b,c = map(int,input().split())
l = [a,b,c]
mx = max(l)
mi = min(l)
l.remove(max(l))
l.remove(min(l))
m = l[0]
d = (mx-m)+(m-mi)
print(d)