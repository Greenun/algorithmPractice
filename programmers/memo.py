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
            print(f"v: {visited}, n: {next_nodes}")
            _, current = heapq.heappop(next_nodes)
            if not current in visited:
                break
    return len([town for town in table if table[town] <= K])

if __name__ == '__main__':
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))