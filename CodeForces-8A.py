def check_sequence(flags, first_seq, second_seq):
    first_index = flags.find(first_seq)
    if first_index == -1:
        return False
    second_index = flags.find(second_seq, first_index + len(first_seq))
    return second_index != -1
flags = input().strip() 
first_seq = input().strip()  
second_seq = input().strip() 
is_forward = check_sequence(flags, first_seq, second_seq)
reversed_flags = flags[::-1]
is_backward = check_sequence(reversed_flags, first_seq, second_seq)
if is_forward and is_backward:
    print("both")
elif is_forward:
    print("forward")
elif is_backward:
    print("backward")
else:
    print("fantasy")
