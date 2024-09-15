n = int(input())
l = input()
if n % 2 == 1:
    print('NO')
else:
    if all(x in ['4', '7'] for x in l):
        s1 = sum(int(l[x]) for x in range(n // 2)) 
        s2 = sum(int(l[x]) for x in range(n // 2, n))  
        if s1 == s2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
