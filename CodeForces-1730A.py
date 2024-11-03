def solve():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    mp = {}
    ans = 0
    for num in a:
        if num in mp:
            mp[num] += 1
        else:
            mp[num] = 1

        if mp[num] <= c:
            ans += 1

    print(ans)


t = int(input())
for _ in range(t):
    solve()
