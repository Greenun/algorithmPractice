def solution(n, edge):
    from collections import defaultdict
    nodes = defaultdict(list)
    for s, e in edge:
        nodes[s].append(e)
        nodes[e].append(s)
    queue = [1]
    visited = set()
    distances = [0]*(n+1)
    dist = 0
    visited.add(1)
    while queue:
        current = queue.pop(0)
        for connected in nodes.get(current):
            if connected not in visited:
                visited.add(connected)
                distances[connected] = distances[current] + 1
                if distances[connected] > dist:
                    dist = distances[connected]
                queue.append(connected)
                # print(distances, current)
    # print(visited)
    
    return distances.count(dist)
    # queue = [1] # start
    # visited = []
    # distances = [0]*(n+1)
    # dist = 0
    # while queue:        
    #     current = queue.pop(0)
    #     if current not in visited:
    #         for connected in nodes.get(current):
    #             if connected not in (queue + visited):
    #                 distances[connected] = distances[current] + 1
    #                 dist = distances[connected] if distances[connected] > dist else dist
    #             if connected not in visited:
    #                 queue.append(connected)    
    #     visited.append(current)
    # return distances.count(dist)
