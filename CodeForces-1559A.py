for _ in range(int(input())):
    l = list(map(int,input().split()))
    f = l[0]
    for x in l[1:]:
        f &= x
    print(f)