def solve():
    t = int(input())
    for _ in range(t):
        dp = [0] * 207
        dp[0] = 1
        
        q, d = map(int, input().split())
        if d == 0:
            d += 10
        
        mx = d * 10
        
        for i in range(11): 
            for j in range(mx - (10 * i + d) + 1):
                dp[10 * i + d + j] |= dp[j]
        
        array = list(map(int,input().split()))
        for u in array:
            if u >= mx or dp[u]:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
