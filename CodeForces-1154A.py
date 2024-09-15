x1,x2,x3,x4 = map(int,input().split())
l = [x1,x2,x3,x4]
abc = max(l)
l.remove(abc)
x = abc-l[0]
y = abc-l[1]
z = abc-l[2]
print(x,y,z)