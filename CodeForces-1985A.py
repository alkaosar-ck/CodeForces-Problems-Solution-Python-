for _ in range(int(input())):
    a, b = input().split() 
    f = a[0]
    a = b[0] + a[1:]
    b = f + b[1:]
    print(a, b)
