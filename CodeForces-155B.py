queris = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    queris.append((b, a))

queris.sort(reverse=True)

total = 1  
answer = 0 
for more, add in queris:
    if total > 0:  
        answer += add  
        total += more - 1  
    else:
        break 
print(answer)
