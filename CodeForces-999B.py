n = int(input())
i = input().strip()
divisors = sorted([x for x in range(1, n + 1) if n % x == 0])
new = i 
for x in divisors: 
    new = (new[:x][::-1]) + new[x:]

print(new)