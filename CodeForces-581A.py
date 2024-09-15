a,b = map(int,input().split())
mi = min(a,b)
out1 = mi
remind = max(a,b)-min(a,b)
out2 = remind//2
print(out1,out2)