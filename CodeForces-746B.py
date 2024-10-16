I = int(input())  
from collections import deque
s = input().strip()
d = deque()
if I == 1 or I == 2:
    print(s)
else:
    if I & 1 == 1:
        d.append(s[0])
        for x in range(1, I - 1, 2):
            d.append(s[x])       
            d.appendleft(s[x + 1])
        l = ''.join(d)
        print(l[::-1])
    else:
        d.appendleft(s[0])  
        for x in range(1, I - 1, 2):
            d.append(s[x])       
            d.appendleft(s[x + 1]) 
        d.append(s[-1])
        print(''.join(d))
    