n = int(input())
L = list(map(int, input().split()))
answer = 0
negative_count = 0
zero_count = 0
for x in L:
    if x >=1:
        answer += (x - 1)
    elif x <= -1:
        answer += (abs(x) - 1)
        negative_count += 1
    elif x == 0:
        zero_count += 1
        answer += 1 
if negative_count % 2 == 1 and zero_count == 0:
    answer += 2
print(answer)
