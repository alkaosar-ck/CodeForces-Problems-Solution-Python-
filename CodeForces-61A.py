l = list(map(int, input().strip()))
m = list(map(int, input().strip()))
im = []
 
for i in range(len(l)):
    if l[i] != m[i]:
        im.append('1')
    else:
        im.append('0')
 
print(''.join(im))