def max_increasing_subarray_length(n, array):
    if n == 0:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, n):
        if array[i] > array[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
    if current_length > max_length:
        max_length = current_length
    
    return max_length

n = int(input())
array = list(map(int, input().split()))

print(max_increasing_subarray_length(n, array))
