def solution():
    #n, k = map(int, input().split())
    n = int(input())
    L = list(map(int, input().split()))
    H = list(map(int,input().split()))
    position = {L[i]: i for i in range(n)}
    answer = []
    im = 0
    for i in H:
        idx = position[i]
        if idx >= im:
            answer.append(idx + 1 - im)
            im = idx + 1
        else:
            answer.append(0)

    print(*answer)
def main():
   #  for _ in range(int(input())):
   #      solution()
   solution()
if __name__ == '__main__':
    main()
