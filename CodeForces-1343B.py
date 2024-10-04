t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 != 0:
        print("NO")
    else:
        print("YES")
        evens = [2 * i for i in range(1, n//2 + 1)]
        odds = [2 * i - 1 for i in range(1, n//2)]
        odds.append(((n//2)*((n//2)+1)-sum(odds)))
        print(*evens, *odds)
