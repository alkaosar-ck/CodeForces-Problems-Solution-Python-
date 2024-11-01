i = int(input())
l = list(map(int,input().split()))
left = 0
maximum = 1
for right in range(1,i):
    if l[right]>2*l[right-1]:
        left = right
        maximum = max(maximum,right-left+1)
    else:
        maximum = max(maximum,right-left+1)
print(maximum)