def solution(n, computers):
    from collections import defaultdict, deque
    networks = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                networks[i].append(j)
                networks[j].append(i)
    count = 1
    # BFS
    whole_computers = set(range(n))
    visited = set()
    queue = deque()
    queue.append(0) # init
    while queue:
        computer = queue.popleft()
        if computer not in visited:
            queue.extend(networks[computer])
            visited.add(computer)
        if not queue and not len(visited) == len(whole_computers):
            queue.append((whole_computers - visited).pop())
            count += 1
    return count
