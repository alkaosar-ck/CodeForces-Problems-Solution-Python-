import sys

def solution(n):
    answer = "989"
    if n == 1:
        return "9"
    elif n == 2:
        return "98"
    elif n == 3:
        return "989"
    else:
        answer_list = list(answer)
        for i in range(n - 3):
            answer_list.append(str(i % 10))
        return ''.join(answer_list)

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        results.append(solution(n))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    main()
