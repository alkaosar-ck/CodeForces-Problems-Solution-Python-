for _ in range(int(input())):
    i = int(input())
    l = list(map(int, input().split()))
    l = l[1:]+l[:1]
    print(' '.join(map(str,l)))