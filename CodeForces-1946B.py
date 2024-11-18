MOD = int(1e9 + 7)

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    S = 0
    sum_all = 0
    cur = 0
    
    for i in range(n):
        sum_all += a[i]
        cur += a[i]
        cur = max(cur, 0) 
        S = max(S, cur) 
    
    sum_all = (sum_all % MOD)
    S = S % MOD
    
    t = 1
    for _ in range(k):
        t = t * 2 % MOD
    
    ans = (sum_all + S * t - S) % MOD
    print(ans)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
