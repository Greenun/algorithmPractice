import sys
from collections import deque, defaultdict

def solution(n, m, matrix):
	global_visited = set()
	area_map = dict()
	info = defaultdict(set)
	area_count = 0
	delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	AIR = 0
	for i in range(n):
		for j in range(m):
			start = (i, j)
			start_value = matrix[i][j]
			if start in global_visited:
				continue
			queue = deque()
			visited = set()
			queue.append(start)
			visited.add(start)
			while queue:
				current = queue.popleft()
				cx, cy = current
				for adj in [(cx + dx, cy + dy) for dx, dy in delta if 0 <= cx + dx < n and 0 <= cy + dy < m]:
					ax, ay = adj
					if (not adj in visited) and matrix[ax][ay] == start_value:
						queue.append(adj)
						visited.add(adj)
			global_visited = global_visited.union(visited)
			if not area_count == AIR:
				info[start_value].add(area_count)
			area_map[area_count] = visited
			area_count += 1
	epoch = 0
	while len(area_map[AIR]) < n*m:
		removed = set()
		for one in info.get(1):
			area = area_map.get(one)
			# check points will be removed
			for point in area:
				px, py = point
				if matrix[px][py] == 0:
					continue
				count = 0
				for adj in [(px + dx, py + dy) for dx, dy in delta if 0 <= px + dx < n and 0 <= py + dy < m]:
					ax, ay = adj
					if matrix[ax][ay] == 0 and adj in area_map[AIR]:
						count += 1
				if count >= 2:
					removed.add(point)
		# update air area
		for point in removed:
			px, py = point
			for adj in [(px + dx, py + dy) for dx, dy in delta if 0 <= px + dx < n and 0 <= py + dy < m]:
				ax, ay = adj
				if matrix[ax][ay] == 0:
					if adj in area_map[AIR]:
						continue
					else:
						target = -1
						for k in area_map.keys():
							if adj in area_map.get(k):
								target = k
								break
						area_map[AIR].update(area_map.get(target))
						area_map.get(target).clear()
			area_map[AIR].add(point)
			matrix[px][py] = 0
		epoch += 1
	return epoch

if __name__ == '__main__':
	n, m = map(int, sys.stdin.readline().replace('\n', '').split(' '))
	matrix = list()
	for _ in range(n):
		matrix.append(list(map(int, sys.stdin.readline().replace('\n', '').split(' '))))
	print(solution(n, m, matrix))

# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0