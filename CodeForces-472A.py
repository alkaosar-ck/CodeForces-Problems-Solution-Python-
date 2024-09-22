i = int(input())

def check(n):

    if n < 2:
        return False  
    is_prime = True
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:  
            is_prime = False
            break
    return is_prime

for x in range(4, 20):
    if not check(x) and not check(i - x):
        print(x, i - x)
        break
