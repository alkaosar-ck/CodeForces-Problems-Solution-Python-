for _ in range(int(input())):
    n, m = map(int, input().split())
    L = max(map(int, input().split()))
    for i in range(m):
        s, l, r = input().split()
        l = int(l)
        r = int(r)
        if l <= L <= r:
            if s == '+':
                L += 1
            else:
                L -= 1
        print(L, end=' ' if i != m-1 else '\n')
 