s = input().strip()
t = input().strip()
ns = ''.join(reversed(s))
if ns == t:
    print('YES')
else:
    print('NO')