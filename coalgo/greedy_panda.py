import sys
from collections import deque, defaultdict
import heapq

sys.setrecursionlimit(300000)

def solution(n, forest):
	answer = 0
	global table
	table = [[0]*n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			answer = max(answer, DFS(forest, n, i, j))
	return answer

def DFS(forest, n, x, y):
	if table[x][y]:
		return table[x][y]
	# print(table)
	table[x][y] = 1
	adjs = [(ax, ay) for ax, ay in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if 0 <= ax < n and 0 <= ay < n]
	for ax, ay in adjs:
		if forest[ax][ay] < forest[x][y]:
			table[x][y] = max(table[x][y], DFS(forest, n, ax, ay) + 1)
	return table[x][y]

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	forest = list()
	for _ in range(n):
		forest.append(list(map(int, sys.stdin.readline().replace('\n', '').split(' '))))
	print(solution(n, forest))


# 시간 초과
# def solution(n, forest):
# 	result_map = dict()
# 	for i in range(n):
# 		for j in range(n):
# 			start = (i, j)
# 			queue = deque()
# 			queue.append(start)
# 			depth = 1
# 			while 1:
# 				temp = deque()
# 				while queue:
# 					cx, cy = queue.popleft()
# 					adjs = [(x, y) for x, y in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)] if 0 <= x < n and 0 <= y < n]
# 					for adj in adjs:
# 						ax, ay = adj
# 						if forest[ax][ay] > forest[cx][cy]:
# 							temp.append(adj)
# 				if not temp:
# 					break
# 				queue = deepcopy(temp)
# 				depth += 1
# 			result_map[(i, j)] = depth
# 	return max(result_map.values())

# 87% 시간초과
# def solution(n, forest):
# 	point_map = defaultdict(list)
# 	ordered = list()
# 	table = [[1]*n for _ in range(n)]
# 	for i in range(n):
# 		for j in range(n):
# 			point_map[forest[i][j]].append((i, j))
# 			heapq.heappush(ordered, forest[i][j])
# 	while ordered:
# 		current = heapq.heappop(ordered)
# 		cx, cy = point_map[current].pop(0)
# 		adjs = [(x, y) for x, y in [(cx+1, cy), (cx-1, cy), (cx, cy-1), (cx, cy+1)] if 0 <= x < n and 0 <= y < n]
# 		for ax, ay in adjs:
# 			if forest[ax][ay] > forest[cx][cy]:
# 				table[ax][ay] = max(table[ax][ay], table[cx][cy] + 1)
# 	return max([max(line) for line in table])

# def solution(n, forest):
# 	point_map = defaultdict(list)
# 	ordered = list()
# 	table = [[1]*n for _ in range(n)]
# 	for i in range(n):
# 		for j in range(n):
# 			point_map[forest[i][j]].append((i, j))
# 			heapq.heappush(ordered, forest[i][j])
# 	while ordered:
# 		current = heapq.heappop(ordered)
# 		cx, cy = point_map[current].pop()
# 		adjs = [(x, y) for x, y in [(cx+1, cy), (cx-1, cy), (cx, cy-1), (cx, cy+1)] if 0 <= x < n and 0 <= y < n]
# 		for ax, ay in adjs:
# 			if forest[ax][ay] > forest[cx][cy]:
# 				table[ax][ay] = max(table[ax][ay], table[cx][cy] + 1)
# 	return max([max(line) for line in table])