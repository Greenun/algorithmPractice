# 진짜 딱 하나 실패ㅡㅡ
def solution(stones, k):
    max_value = max(stones[0:k])
    count = max_value
    for i in range(1, len(stones) + 1 - k):
        if stones[i-1] == max_value:
            max_value = max(stones[i:i+k])
        else:
            max_value = stones[i+k-1] if stones[i+k-1] > max_value else max_value
        if max_value < count:
            count = max_value
    return count

def solution(stones, k):
    low = 1
    high = max(stones)
    while low < high:
        mid = (low + high) // 2
        cont = 0
        temp = 0
        for stone in stones:
            if stone - mid <= 0:
                temp += 1
            else:
                cont = temp if temp > cont else cont
                temp = 0
        cont = temp if temp > cont else cont
        if cont >= k:
            high = mid
        else:
            low = mid + 1
    return low
            