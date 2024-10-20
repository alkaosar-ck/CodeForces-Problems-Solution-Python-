def solve3(n):
    if n % 2 == 1:
        return [1, n // 2, n // 2]
    if n % 4 == 0:
        return [n // 2, n // 4, n // 4]
    if n % 2 == 0:
        return [2, n // 2 - 1, n // 2 - 1]

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    added = solve3(n - k + 3)
    for i in range(k):
        print(added[i] if i < 3 else 1, end=' ')
    print()
