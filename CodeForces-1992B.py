t = int(input())  
for _ in range(t):
    n, k = map(int, input().split()) 
    a = list(map(int, input().split()))  
    m = max(a)
    c= a.copy()
    c.remove(m)
    from collections import Counter
    count = Counter(c)
    times1 = 0
    others = 0
    times1 = count[1]
    for x in c:
       if x != 1:
          others += (x-1)+(x)
    print(times1+others)