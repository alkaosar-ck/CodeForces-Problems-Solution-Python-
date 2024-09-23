t = int(input())  # Number of cupboards
left_open = 0
right_open = 0
for _ in range(t):
    l, r = map(int, input().split())
    left_open += l  
    right_open += r  
min_left_moves = min(left_open, t - left_open)
min_right_moves = min(right_open, t - right_open)
total_moves = min_left_moves + min_right_moves
print(total_moves)
