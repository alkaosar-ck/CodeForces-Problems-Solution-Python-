from collections import defaultdict, deque

def solution():
    n, m = map(int, input().split())
    cats = list(map(int, input().split()))
    graph = defaultdict(list)

    for _ in range(n - 1):
        x, y = map(int, input().split())
        x -= 1 
        y -= 1 
        graph[x].append(y)
        graph[y].append(x)

    stack = [(0, -1, cats[0])]  
    result = 0

    while stack:
        v, parent, k = stack.pop()

        if k > m:
            continue

        is_leaf = True

        for neighbor in graph[v]:
            if neighbor != parent:
                is_leaf = False
                stack.append((neighbor, v, k + 1 if cats[neighbor] else 0))

        if is_leaf:
            result += 1

    print(result)

def main():
    solution()

if __name__ == '__main__':
    main()
