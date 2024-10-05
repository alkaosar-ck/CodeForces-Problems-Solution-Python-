for _ in range(int(input())):
    n = int(input())  
    candies = list(map(int, input().split())) 
    oranges = list(map(int, input().split()))
    min_can = min(candies)
    min_ora = min(oranges)
    total_moves = 0
    for i in range(n):
        extra_candies = candies[i] - min_can
        extra_oranges = oranges[i] - min_ora
        simultaneous_moves = min(extra_candies, extra_oranges)
        total_moves += simultaneous_moves  
        total_moves += (extra_candies - simultaneous_moves)
        total_moves += (extra_oranges - simultaneous_moves) 
    print(total_moves)
