def solution(s):
    max_value = 0
    n = len(s)
    for low in range(len(s)):
        if n - low < max_value: break
        high = len(s) - 1
        while low <= high:
            if s[low] == s[high]:
                if check(s[low:high+1]):
                    max_value = high - low + 1 if max_value < high - low + 1 else max_value
            high -= 1
    return max_value
        

def check(substring):    
    low = 0
    high = len(substring) - 1
    while low < high:
        if not substring[low] == substring[high]:
            return False
        low += 1
        high -= 1
    return True