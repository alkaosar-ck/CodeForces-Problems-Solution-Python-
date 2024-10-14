i = int(input())
L = list(map(int,input().split()))
evens = sorted([x for x in L if x&1 == 0])
odds = sorted([x for x in L if x&1 == 1])
m = min(len(evens),len(odds))
for _ in range(m):
   evens.pop()
   odds.pop()
if evens:
   evens.pop()
if odds:
   odds.pop()
total = sum(evens)+sum(odds)
print(total)