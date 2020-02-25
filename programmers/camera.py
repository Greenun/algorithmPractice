# 시간 초과
def solution(routes):
    import heapq
    count = 0
    queue = list()
    for rst, red in routes:
        heapq.heappush(queue, (rst - red, (rst, red)))
    while 1:
        _, (st, ed) = heapq.heappop(queue)
        if not [st, ed] in routes:
            continue
        count += 1
        comp = list()
        prev
        for point in range(st, ed + 1):
            x = list()
            for rst, red in routes:
                if point >= rst and point <= red:
                    x.append([rst, red])
            comp.append(x)
        
        for c in comp[max_idx]:
            routes.remove(c)
        if not routes:
            break
    return count
                

# 힌트를 바탕으로 다시(통과)
def solution(routes):
    import heapq
    count = 1
    queue = list()
    for rst, red in routes:
        heapq.heappush(queue, (rst, (rst, red)))
    prev = list()
    while 1:
        if not queue:
            break
        _, (st, ed) = heapq.heappop(queue)
        if not [st, ed] in routes:
            continue
        point = st
        for pst, ped in prev:
            if point <= ped and point >= pst:
                pass
            else:
                count += 1
                prev = list()
                break
        prev.append([st, ed])
    return count
                