
 
for i in range(int(input())):
    (a1, k) = map(int, input().split())
    for e in range(k - 1):
        largest = int(max(str(a1)))
        smallest = int(min(str(a1)))
        if smallest != 0:
            a1 += largest * smallest
        else:
            break
 
    print(a1)