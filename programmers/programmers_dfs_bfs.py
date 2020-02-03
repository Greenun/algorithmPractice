def solution(n, computers):
    answer = 0
    from collections import defaultdict
    nodes = defaultdict(set)
    for i in range(n):
        for j in range(n):
            if i <= j: continue
            if computers[i][j] == 1:
                nodes[i].add(j)
                nodes[j].add(i)
    node_set = set(range(0, n))
    
    queue = [0]
    visited = set()
    visited.add(0)
    count = 1
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
        for connected in nodes[current]:
            if connected not in visited:
                queue.append(connected)
                visited.add(connected)
        if not queue and n > len(visited):
            print(visited, node_set, queue)
            node_set -= visited
            count += 1
            queue.append(node_set.pop())
            print(queue)
    print(count)
    return answer


if __name__ == '__main__':
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])