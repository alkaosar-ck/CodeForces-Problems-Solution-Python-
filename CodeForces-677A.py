n,h = map(int,input().split())
l = list(map(int,input().split()))
w = 0
for x in l:
    if x>h:
        w+=2
    elif x<=h:
        w+=1
print(w)