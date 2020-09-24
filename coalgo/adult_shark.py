import sys
from collections import defaultdict, OrderedDict
from copy import deepcopy

def solution(board, sharks, priority, d):	
	n = len(board)
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
	temp = dict()
	keys = sorted(sharks.keys(), reverse = True)
	counter = defaultdict(int)

	for i in range(0, 1001):
		# out
		temp_keys = keys[:]
		if temp:
			for k in temp_keys:
				if k not in temp.values():
					keys.remove(k)
					sharks.pop(k)
		if len(keys) == 1:
			return i
		temp.clear()
		for k in keys:
			# before move (scent)
			current, _ = sharks[k]
			x, y = current
			counter[(x, y)] = d
			board[x][y] = k
		
		for k in keys:
			current, direction = sharks[k]
			x, y = current
			# move
			prior = priority[k][direction]
			nx = -3
			ny = -3
			np = -1
			for p in prior:
				dx, dy = directions[p-1]
				if not 0 <= x + dx < n or not 0 <= y + dy < n: continue
				if board[x + dx][y + dy] == 0:
					nx = x + dx
					ny = y + dy
					np = p - 1
					break
			if np == -1:
				for p in prior:
					dx, dy = directions[p-1]
					if not 0 <= x + dx < n or not 0 <= y + dy < n: continue
					if board[x + dx][y + dy] == k:
						nx = x + dx
						ny = y + dy
						np = p - 1
						break
			# after move
			sharks[k] = ((nx, ny), np)
			temp[(nx, ny)] = k
		for k in counter:
			counter[k] -= 1
			if counter[k] <= 0:
				x, y = k
				board[x][y] = 0
	return -1

if __name__ == '__main__':
	n, m, k = map(int, sys.stdin.readline().replace('\n', '').split(' '))
	board = list()
	sharks = dict()
	priority = defaultdict(dict)
	for _ in range(n):
		board.append(list(map(int, sys.stdin.readline().replace('\n', '').split(' '))))

	idx = 1
	for i in range(n):
		for j in range(n):
			if idx > m: break
			if not board[i][j] == 0:
				sharks[board[i][j]] = (i, j)
				idx += 1
	for i, v in enumerate(map(int, sys.stdin.readline().replace('\n', '').split(' '))):
		origin = sharks[i+1]
		sharks[i+1] = (origin, v - 1)
	for i in range(4, 4*(m+1)):
		priority[i // 4][i % 4] = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	print(solution(board, sharks, priority, k))
