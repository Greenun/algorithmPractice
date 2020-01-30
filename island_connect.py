def solution(n, costs):
    from collections import defaultdict
    # cost_dict = defaultdict(list)
    node_map = defaultdict(list)
    cost_dict = defaultdict(int)
    # bridges = list()
    cost_sum = 0
    cost_list = list()
    for c in costs:
        node_map[c[0]].append(c[1])
        node_map[c[1]].append(c[0])
        cost_list.append(c[2])
        cost_dict[(c[0], c[1])] = c[2]
        # cost_dict[c[2]].append((c[0], c[1]))
        # bridges.append((c[0], c[1]))
    m = min(cost_list)
    visited = list()
    # cost_list = cost_dict.keys()
    # temp = min(cost_list)
    for c in costs:
        if c[2] == m:
            target = [c[0], c[1]]
            break
    cost_sum += m
    visited += target
    node_map[visited[0]].remove(visited[1])
    while len(visited) < n:
        print('visited: ', visited)
        targets = []
        for v in visited:
            for t in node_map[v]:
                targets.append((v, t))
        print("targets: ", targets)
        print("node_map: ", node_map)
        min_bridge, min_cost = find_min(cost_dict, targets)
        cost_sum += min_cost
        visited.append(min_bridge[1])
        print(visited, min_bridge)
        node_map[min_bridge[0]].remove(min_bridge[1])
        node_map[min_bridge[1]].remove(min_bridge[0])
    return cost_sum

def find_min(cost_dict, targets):
    min_cost = (targets[0], cost_dict[targets[0]])
    for target in targets[1:]:
        if min_cost[1] > cost_dict[target]:
            min_cost = (target, cost_dict[target])
    return min_cost[0], min_cost[1]

if __name__ == '__main__':
    solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
    solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [2, 4, 3], [1, 3, 4]])
    solution(7, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [2, 4, 3], [5, 6, 2], [1, 3, 4], [4, 5, 5]])