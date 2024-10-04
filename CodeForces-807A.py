n = int(input())
l = []
rated = False

for _ in range(n):
    a, b = map(int, input().split())
    l.append(a)
    if a != b: 
        rated = True

if rated:
    print("rated")
else:
    if l != sorted(l, reverse=True): 
        print("unrated")
    else:
        print("maybe")
