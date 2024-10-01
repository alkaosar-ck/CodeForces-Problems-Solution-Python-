for _ in range(int(input())):
    x, y, n = map(int, input().split())
    k = (n - y) // x * x + y
    if k > n:
        k -= x
    
    print(k)
