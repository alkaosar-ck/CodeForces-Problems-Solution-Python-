def is_lucky_number(num):
    for digit in str(num):
        if digit != '4' and digit != '7':
            return False
    return True
 
def is_nearly_lucky_number(n):
    n_str = str(n)
    
    lucky_digit_count = 0
    for digit in n_str:
        if digit == '4' or digit == '7':
            lucky_digit_count += 1

    if is_lucky_number(lucky_digit_count):
        return "YES"
    else:
        return "NO"
n = input().strip()
print(is_nearly_lucky_number(n))