def count_QAQ(s):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == 'A':
            left_Q = s[:i].count('Q') 
            right_Q = s[i+1:].count('Q') 
            count += left_Q * right_Q
    return count
s = input() 
print(count_QAQ(s))
