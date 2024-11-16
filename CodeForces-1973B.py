import sys
input = sys.stdin.read

def check(v, mid, ori):
    frekbit = [0] * 31
    for i in range(mid):
        x = v[i]
        for j in range(30, -1, -1):
            if x >= (1 << j):
                x -= (1 << j)
                frekbit[j] += 1
    
    or2 = 0
    for i in range(31):
        if frekbit[i] > 0:
            or2 += (1 << i)
    
    if or2 != ori:
        return False

    for i in range(1, len(v) - mid + 1):
        x = v[i - 1]
        for j in range(30, -1, -1):
            if x >= (1 << j):
                x -= (1 << j)
                frekbit[j] -= 1
                if frekbit[j] == 0:
                    or2 -= (1 << j)
        
        x = v[i + mid - 1]
        for j in range(30, -1, -1):
            if x >= (1 << j):
                x -= (1 << j)
                frekbit[j] += 1
                if frekbit[j] == 1:
                    or2 += (1 << j)
        
        if or2 != ori:
            return False

    return True

def solution():
    data = input().strip().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        v = list(map(int, data[index + 1:index + 1 + n]))
        index += n + 1
        
        ori = 0
        for num in v:
            ori |= num
        
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if check(v, mid, ori):
                hi = mid
            else:
                lo = mid + 1
        
        results.append(str(lo))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solution()
