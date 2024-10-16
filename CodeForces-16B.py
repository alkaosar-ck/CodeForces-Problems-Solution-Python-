import heapq
n, m = map(int, input().split())
main = []
heapq.heapify(main)
for _ in range(m):
    ai, bi = map(int, input().split())
    heapq.heappush(main, (-bi, ai)) 
total = 0
while n > 0 and main:
    value, count = heapq.heappop(main)
    take = min(n, count)
    total -= value * take  
    n -= take  
print(total)
