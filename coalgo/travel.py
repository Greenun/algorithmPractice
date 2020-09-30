import sys
from collections import defaultdict, deque

def solution(matrix, plan):
	city_map = defaultdict(set)
	for i in range(len(matrix)):
		for j in range(i, len(matrix)):
			if matrix[i][j] == '1':
				city_map[str(i+1)].add(str(j+1))
				city_map[str(j+1)].add(str(i+1))
	
	start = plan.pop(0)
	visited = set()
	queue = deque()
	queue.append(start)
	visited.add(start)
	while queue:
		current = queue.popleft()
		for adj in city_map[current]:
			if adj not in visited:
				queue.append(adj)
				visited.add(adj)
	
	for p in plan:
		if p not in visited:
			return "NO"
	return "YES"


if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	m = int(sys.stdin.readline().strip())
	matrix = list()
	for i in range(n):
		matrix.append(sys.stdin.readline().replace('\n', '').split(' '))
	plan = sys.stdin.readline().replace('\n', '').split(' ')
	print(solution(matrix, plan))
# 5
# 5
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 5 3 2 3 4