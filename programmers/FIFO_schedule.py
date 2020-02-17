# 우선순위 큐 방식 - 시간 초과
def solution(n, cores):
    import heapq
    idle_queue = list()
    working_queue = list()
    for idx, core in enumerate(cores):
        heapq.heappush(idle_queue, (idx, core))
    now = 0
    while n > 0:
        if idle_queue:
            core = heapq.heappop(idle_queue)
            if n == 1:
                return core[0] + 1
            heapq.heappush(working_queue, (now + core[1], core))
            n -= 1
        else:            
            t, core = heapq.heappop(working_queue)
            now = t
            heapq.heappush(idle_queue, core)
            t, core = working_queue[0]
            while now == t:
                t, core = heapq.heappop(working_queue)
                heapq.heappush(idle_queue, core)
                if not working_queue:
                    break
                t, core = working_queue[0]

# parametric search
# binary search end 지점 파악 중요.
def solution(n, cores):
    init = len(cores)
    # a_t = init + [for all t // cores]
    m = min(cores)
    low = (m * n) // init
    high = (max(cores) * n) // init
    while low < high:
        mid = (low + high) // 2
        a_t = init + sum([mid // core for core in cores])
        if a_t > n:
            high = mid
        else:
            low = mid + 1
    target = low
    a_t = init + sum([target // core for core in cores])
    enable = [idx for idx, core in enumerate(cores) if target % core == 0]
    a_t -= len(enable) # a_t 는 enable을 추가하기 이전의 값
    while a_t >= n:
        # print(enable, target, a_t, n)
        target -= 1
        enable = [idx for idx, core in enumerate(cores) if target % core == 0]
        if len(enable) > 0:
            a_t -= len(enable)
    # print(enable, target, a_t, n)
    return enable[n - a_t - 1] + 1
    
