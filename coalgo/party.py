import sys
from collections import defaultdict, deque
import heapq

def solution(n, m, x, roads, reversed_roads, cost_map):
	cost_table = [float('inf')]*n
	
	cost_table[x-1] = 0
	order = list()
	heapq.heappush(order, (0, x))
	while order:
		cost, current = heapq.heappop(order)
		for adj in roads[current]:
			adj_cost = cost_map[(current, adj)]
			if cost_table[adj-1] > cost_table[current-1] + adj_cost:
				cost_table[adj-1] = cost_table[current-1] + adj_cost
				heapq.heappush(order, (cost_table[adj-1], adj))

	reversed_cost = [float('inf')]*n
	reversed_cost[x-1] = 0
	order = list()
	heapq.heappush(order, (0, x))

	while order:
		cost, current = heapq.heappop(order)
		for adj in reversed_roads[current]:
			adj_cost = cost_map[(adj, current)]
			if reversed_cost[adj-1] > reversed_cost[current - 1] + adj_cost:
				reversed_cost[adj-1] = reversed_cost[current - 1] + adj_cost
				heapq.heappush(order, (reversed_cost[adj-1], adj))
	
	return max([cost_table[i] + reversed_cost[i] for i in range(n)])

if __name__ == '__main__':
	n, m, x = map(int, sys.stdin.readline().replace("\n", "").split(" "))
	roads = defaultdict(set)
	cost_map = dict()
	reversed_roads = defaultdict(set)

	for _ in range(m):
		st, ed, cost = map(int, sys.stdin.readline().replace("\n", "").split(" "))
		roads[st].add(ed)
		reversed_roads[ed].add(st)
		cost_map[(st, ed)] = cost
	print(solution(n, m, x, roads, reversed_roads, cost_map))