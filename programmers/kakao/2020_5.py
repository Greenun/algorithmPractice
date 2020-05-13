def solution(n, path, order):
    from collections import defaultdict
    path_map = defaultdict(list)
    for s, e in path:
        path_map[s].append(e)
        path_map[e].append(s)
    stack = [0]
    visited = set()
    order_end = [o[1] for o in order]
    order_need = [o[0] for o in order]
    loop = 0
    while stack:
        current = stack.pop()
        if current in order_end:
            if not order_need[order_end.index(current)] in visited:
                stack.insert(0, current)
                loop += 1
                if loop > len(stack): break
                continue
        ables = [x for x in path_map[current] if x not in visited]
        stack.extend(ables)
        visited.add(current)
        loop = 0
    return len(visited) == n

