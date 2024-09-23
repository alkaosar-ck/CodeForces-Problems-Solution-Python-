for _ in range(int(input())):
    n = int(input())
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    if min_x < 0 and max_x > 0 and min_y < 0 and max_y > 0:
        print("NO")
    else:
        print("YES")
