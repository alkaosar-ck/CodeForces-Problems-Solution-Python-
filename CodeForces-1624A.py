for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mi = min(arr)
    mx = max(arr)
    print(mx-mi)
