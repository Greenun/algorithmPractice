def solution(jobs):
    import heapq
    n = len(jobs)
    task_queue = list()
    current = 0
    elapsed_sum = 0
    # 실행 시간이 같은 경우 e[1] 까지 정렬
    jobs.sort(key=lambda e: (e[0], e[1]))
    idx = 0
    while 1:
    	# task queue update
    	# current가 작아서 추가를 못하는 경우 작업 수행
        if idx >= len(jobs): break
        job = jobs[idx]
        if current >= job[0]:
            heapq.heappush(task_queue, (job[1], job))
            idx += 1
        else:
            if not task_queue:
                current = job[0]
                elapsed_sum += current + job[1] - job[0]
                current += job[1]
                idx += 1
            else:
                value = heapq.heappop(task_queue)[1]
                elapsed_sum += current + value[1] - value[0]
                current += value[1]
    while task_queue:
        value = heapq.heappop(task_queue)[1]
        elapsed_sum += current + value[1] - value[0]
        current += value[1]
    return elapsed_sum // n
        
    