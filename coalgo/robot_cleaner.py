import sys

def solution(board, start, direction):
	moves = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
	cleaned = 0
	visited = set()
	current = start
	while 1:
		x, y = current
		if current not in visited:
			visited.add(current)
			cleaned += 1
		dx, dy = moves[(direction - 1) % 4]
		nx = x + dx
		ny = y + dy
		# print(current, (nx, ny), direction)
		all_directions = [(x + xx, y + yy) for xx, yy in moves]
		# print(all_directions, current, direction)
		# print([d in visited or board[d[0]][d[1]] == 1 for d in all_directions])
		# c
		if all([d in visited or board[d[0]][d[1]] == 1 for d in all_directions]):
			bx, by = moves[(direction + 2) % 4]
			back = (x + bx, y + by)
			# print(back)
			if board[back[0]][back[1]] == 1:
				break
			else:
				current = back
				continue
		# b
		if (nx, ny) in visited or board[nx][ny] == 1:
			direction = (direction - 1) % 4 # turn left
			continue
		# a
		if (nx, ny) not in visited:
			direction = (direction - 1) % 4 # turn left
			current = (nx, ny)
			continue
	return cleaned

if __name__ == '__main__':
	n, m = map(int, sys.stdin.readline().replace("\n", "").split(' '))
	x, y, direction = map(int, sys.stdin.readline().replace("\n", "").split(' '))
	board = list()
	for _ in range(n):
		board.append(list(map(int, sys.stdin.readline().replace("\n", "").split(' '))))
	print(solution(board, (x, y), direction))