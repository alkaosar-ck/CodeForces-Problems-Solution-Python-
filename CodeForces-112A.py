s1 = input().strip()
s2 = input().strip()
slow = s1.lower()
s2low = s2.lower()
if slow<s2low:
    print(-1)
elif slow>s2low:
    print(1)
else: 
    print(0)
