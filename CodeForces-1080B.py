def F(x):
    if x % 2 == 0:
        return x // 2
    else:
        return -x + F(x - 1)

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(F(r) - F(l - 1))
