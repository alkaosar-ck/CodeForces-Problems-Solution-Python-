def solve():
    n, m = map(int, input().split())  
    grid = [list(input().strip()) for _ in range(n)] 
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    move_char = ['U', 'R', 'D', 'L']
    
    start_row, start_col = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start_row, start_col = i, j
                break
        if start_row != -1:
            break
    
    visited = [[False] * m for _ in range(n)]
    visited[start_row][start_col] = True
    path = []

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '*' and not visited[x][y]
   
    current_row, current_col = start_row, start_col
    visited[current_row][current_col] = True
    while True:
        found_next = False
        for d, (dx, dy) in enumerate(directions):
            next_row, next_col = current_row + dx, current_col + dy
            if is_valid(next_row, next_col):
                visited[next_row][next_col] = True
                path.append(move_char[d])
                current_row, current_col = next_row, next_col
                found_next = True
                break
        
        if not found_next:
            break

    for d, (dx, dy) in enumerate(directions):
        next_row, next_col = current_row + dx, current_col + dy
        if next_row == start_row and next_col == start_col:
            path.append(move_char[d])
            break

    print(''.join(path))

solve()
