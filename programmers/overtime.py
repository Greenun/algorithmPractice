# 효율성 실패
def solution(n, works):
    works.sort(reverse=True)
    
    while n > 0:
        works[0] -= 1
        for i in range(len(works) - 1):
            if works[i] >= works[i+1]:
                break
            else:
                works[i], works[i+1] = works[i+1], works[i]
        n -= 1
    return sum([work**2 for _, work in work_heap if work > 0])

# 효율성 통과
def solution(n, works):
    import heapq
    work_heap = list()
    for work in works:
        heapq.heappush(work_heap, (-1*work, work))
    while n > 0:
    	# 가장 큰 값
        _, first = heapq.heappop(work_heap)
        # 두 번째가 없으면 빼고 종료
        if len(work_heap) == 0:
            heapq.heappush(work_heap, (0, first - n))
            n = -1
            break
        # 두번 째 큰 값
        _, second = work_heap[0]
        if first - second >= n:
            first -= n
            heapq.heappush(work_heap, (-1*first, first))
            n = -1
            break
        else:
        	# 1번 - 2번 == 0 이면 --> 1만 빼고 이외의 경우 1번 - 2번의 크기만큼 빼기
            interval = first - second if not first == second else 1
            temp = first - interval
            heapq.heappush(work_heap, (-1*temp, temp))
            n -= interval
    return sum([work**2 for _, work in work_heap if work > 0])
