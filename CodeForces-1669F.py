for _ in range(int(input())):
    i = int(input()) 
    l = list(map(int, input().split())) 
    m, r = 0, i - 1  
    sum_left, sum_right = l[m], l[r] 
    max_candies = 0  
    while m < r:
        if sum_left == sum_right:
        
            max_candies = max(max_candies, (m + 1) + (i - r))
          
            m += 1
            r -= 1
            if m < r:
                sum_left += l[m]
                sum_right += l[r]
        elif sum_left < sum_right:
        
            m += 1
            sum_left += l[m]
        else:
          
            r -= 1
            sum_right += l[r]

    print(max_candies)
