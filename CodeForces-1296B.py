for _ in range(int(input())):
    s = int(input())
    total = 0
    while s >= 10:
        total += s - s % 10 
        s = s // 10 + s % 10 
    total += s 
    print(total)
