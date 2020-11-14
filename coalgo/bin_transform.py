def solution(s):
    count = 0
    zeros = 0
    while len(s) > 1:
        temp, s = rm_zero(s)
        s = to_bin(s)
        count += 1
        zeros += temp
        
    return [count, zeros]
        
def to_bin(target):
    return bin(len(target))[2:]

def rm_zero(target):
    count = 0
    new_c = ""
    for c in target:
        if c == '0':
            count += 1
        else:
            new_c += c
    return count, new_c