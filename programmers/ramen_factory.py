def solution(stock, dates, supplies, k):
    import heapq
    supply_heap = list()
    for idx, supply in enumerate(supplies):
        heapq.heappush(supply_heap, (-1*supply, (dates[idx], supply)))
    
    while stock < k:
        temp = list()
        for i in range(len(supply_heap)):
            value = heapq.heappop(supply_heap)[1]
            if stock >= value[0]:
                stock += value[1]
                break
            else:
                temp.append(value)
        for t in temp:
            heapq.heappush(supply_heap, (-1*t[1], t))
    return len(supplies) - len(supply_heap)