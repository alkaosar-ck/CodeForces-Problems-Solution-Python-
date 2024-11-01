for _ in range(int(input())):
    size,limit = map(int,input().split())
    fruits = list(map(int,input().split()))
    heights = list(map(int,input().split()))
    prefix_sum = [0]*(size+1)
    for x in range(size):
        prefix_sum[x+1] = prefix_sum[x]+fruits[x]
    max_length = 0
    left = 0
    for right in range(size):
        if right>0 and heights[right-1]%heights[right] != 0:
            left = right
        current_sum = prefix_sum[right+1] -  prefix_sum[left]
        if current_sum<=limit:
            max_length = max(max_length,right-left+1)
        else:
            while current_sum>limit and left<=right:
                left+=1
                current_sum = prefix_sum[right+1]-prefix_sum[left]
    print(max_length)