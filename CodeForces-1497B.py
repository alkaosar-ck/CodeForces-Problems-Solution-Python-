from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    
    hash_map = defaultdict(int)
    for x in l:
        hash_map[x % m] += 1
    
    total = 0
    
    if hash_map[0]:
        total += 1
    
    for x in range(1, (m // 2) + 1):
        if x == m - x:
            if hash_map[x] > 0:
                total += 1
        else:
            count_x = hash_map[x]
            count_mx = hash_map[m - x]
            
            if count_x > 0 or count_mx > 0:
                total += 1 + max(0, abs(count_x - count_mx) - 1)
    
    print(total)
