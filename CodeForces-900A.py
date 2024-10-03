n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
count_positive = sum(1 for x, y in points if x > 0)
count_negative = sum(1 for x, y in points if x < 0)
if count_positive <= 1 or count_negative <= 1:
    print("Yes")
else:
    print("No")
