# 하나 틀림...
def solution(N, road, K):
    from collections import defaultdict
    maps = defaultdict(set)
    table = dict()
    table[1] = 0
    for i in range(1, N):
        table[i+1] = 500100
    for st, ed, t in road:
        maps[st].add((ed, t))
        maps[ed].add((st, t))
    queue = list()
    queue.append(1)
    visited = set()
    while queue:
        current = queue.pop(0)
        visited.add(current)
        for neighbor, t in maps[current]:
            if table[current] > table[neighbor] + t:
                table[current] = table[neighbor] + t
            elif table[current] + t < table[neighbor]:
                table[neighbor] = table[current] + t
            if not neighbor in visited:
                queue.append(neighbor)
    return len([town for town in table if table[town] <= K])

# 맞춤 - 다익스트라 거의 그대로
def solution(N, road, K):
    from collections import defaultdict
    import heapq
    maps = defaultdict(set)
    table = dict()
    table[1] = 0
    for i in range(1, N):
        table[i+1] = 500100
    for st, ed, t in road:
        maps[st].add((ed, t))
        maps[ed].add((st, t))
    current = 1
    next_nodes = list()
    visited = set()
    while 1:
        visited.add(current)
        for neighbor, t in maps[current]:
            if table[current] + t < table[neighbor]:
                table[neighbor] = table[current] + t
            heapq.heappush(next_nodes, (table[neighbor], neighbor))
        if len(visited) >= N:
            break
        while 1:
            _, current = heapq.heappop(next_nodes)
            if not current in visited:
                break
    return len([town for town in table if table[town] <= K])

# 우선순위 큐(heap) 다익스트라 (더 빠름)
def solution(N, road, K):
    from collections import defaultdict
    import heapq
    maps = defaultdict(set)
    table = dict()
    table[1] = 0
    for i in range(1, N):
        table[i+1] = 500100
    for st, ed, t in road:
        maps[st].add((ed, t))
        maps[ed].add((st, t))
    pqueue = list()
    for node in table:
        heapq.heappush(pqueue, (table[node], node))
    while pqueue:
        ct, current = heapq.heappop(pqueue)
        if ct <= table[current]:
            for neighbor, t in maps[current]:
                if table[neighbor] >= ct + t:
                    table[neighbor] = ct + t
                    heapq.heappush(pqueue, (table[neighbor], neighbor))
    
    return len([town for town in table if table[town] <= K])
        