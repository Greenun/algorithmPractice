def solution(gems):
    category = set(gems)
    length = len(category)
    low = 0
    high = len(gems)
    mid = (low + high) // 2
    while low < mid:
        if not set(gems[mid:high+1]) == category:
            mid = (low + mid) // 2
        else: break
        
    low = mid
    mid = (mid + high) // 2
    while mid < high:
        if not set(gems[low:mid+1]) == category:
            mid = (mid + high) // 2 + 1
        else:
            break
    temp_low, temp_mid = low, mid
    while 1:
        if set(gems[temp_low:temp_mid]) == category:
            temp_mid -= 1
        elif set(gems[temp_low+1:temp_mid+1]) == category:
            temp_low += 1
        else:
            break
    for i in range(1, temp_low + 1):
        if set(gems[temp_low-i:temp_mid-i+1]) == category:
            temp_low -= i
            temp_mid -= i
    
    return [temp_low+1, temp_mid+1]