import sys
from collections import deque
from itertools import combinations

def solution(board):
	n = len(board)
	groups = [[0]*n for _ in range(n)]
	distances = [[-1]*n for _ in range(n)]
	idx = 1
	queue = deque()
	expand_queue = deque()
	for i in range(n):
		for j in range(n):
			if board[i][j] == 1:
				expand_queue.append((i, j))
				if groups[i][j] == 0:
					start = (i, j)
					groups[i][j] = idx
					queue.append(start)
					while queue:
						cx, cy = queue.popleft()
						distances[cx][cy] = 0
						adjs = [(x, y) for x, y in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)] if 0 <= x < n and 0 <= y < n]
						for ax, ay in adjs:
							if board[ax][ay] == 1 and groups[ax][ay] == 0:
								groups[ax][ay] = idx
								queue.append((ax, ay))
					idx += 1
	while expand_queue:
		cx, cy = expand_queue.popleft()
		adjs = [(x, y) for x, y in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)] if 0 <= x < n and 0 <= y < n]
		for ax, ay in adjs:
			if distances[ax][ay] == -1:
				distances[ax][ay] = distances[cx][cy] + 1
				groups[ax][ay] = groups[cx][cy]
				expand_queue.append((ax, ay))
	
	return get_distance(distances, groups)

def get_distance(distances, groups):
	n = len(distances)
	min_distance = float('inf')
	for i in range(n):
		for j in range(n):
			adjs = [(x, y) for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if 0 <= x < n and 0 <= y < n]
			for ax, ay in adjs:
				if not groups[i][j] == groups[ax][ay]:
					distance = distances[i][j] + distances[ax][ay]
					
					if min_distance > distance:
						min_distance = distance
	return min_distance

# # 시간 초과
# def solution2(board):
# 	islands = list()
# 	n = len(board)
# 	start = None
# 	# near_ocean = list()
# 	# temp = [line[:] for line in board]

# 	while not start:
# 		island = set()
# 		# near = set()
# 		for i in range(n):
# 			for j in range(n):
# 				if board[i][j] == 1:
# 					island.add((i, j))
# 					start = (i, j)
# 					board[i][j] = 0
# 					break
# 			if start:
# 				break
# 		if not start:
# 			break
# 		queue = deque()
# 		queue.append(start)
# 		while queue:
# 			x, y = queue.popleft()
# 			adjs = [(ax, ay) for ax, ay in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if 0 <= ax < n and 0 <= ay < n]
# 			for adj in adjs:
# 				adj_x, adj_y = adj
# 				if board[adj_x][adj_y] == 1:
# 					island.add(adj)
# 					board[adj_x][adj_y] = 0
# 					queue.append(adj)
# 			# if not all([temp[adj_x][adj_y] == 1 for adj_x, adj_y in adjs]):
# 				# near.add((x, y))
# 		islands.append(island)
# 		# near_ocean.append(near)
# 		start = None
# 	# idx = 0
# 	# islands[0] = set()
# 	# for i in range(n):
# 	# 	for j in range(n):
# 	# 		if board[i][j] == 1:
# 	# 			keys = list(islands.keys())
# 	# 			for k in keys:
# 	# 				if ((i-1, j) in islands[k]) or ((i, j-1) in islands[k]):
# 	# 					islands[k].add((i, j))
# 	# 					break
# 	# 				else:
# 	# 					if k == keys[-1]:
# 	# 						islands[idx].add((i, j))
# 	# 						idx += 1
# 	min_distance = float('inf')
# 	for comb in combinations(islands, 2):
# 		distance = get_distance(comb[0], comb[1])
# 		if min_distance > distance:
# 			min_distance = distance
# 	return min_distance

# 	# min_distance = float('inf')
	
# 	# for comb in combinations(list(range(len(islands))), 2):
# 	# 	distance = get_distance(near_ocean[comb[0]], near_ocean[comb[1]])
# 	# 	if min_distance > distance:
# 	# 		min_distance = distance
# 	# return min_distance

# def get_distance(f_group, s_group):
# 	min_distance = float('inf')
# 	for fx, fy in f_group:
# 		for sx, sy in s_group:
# 			distance = abs(fx - sx) + abs(fy - sy) - 1
# 			if min_distance > distance:
# 				min_distance = distance
# 	return min_distance

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	board = list()
	for _ in range(n):
		board.append(list(map(int, sys.stdin.readline().replace('\n', '').split(' '))))
	print(solution(board))