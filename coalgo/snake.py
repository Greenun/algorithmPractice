import sys

def solution(n, apples, turn):
	from collections import deque
	area = deque()
	current = (1, 1)
	
	moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
	direction = 0
	count = 0
	while 1:
		count += 1
		area.append(current)
		x, y = current
		
		# move
		dx, dy = moves[direction]
		np = (x + dx, y + dy)
		if x + dx > n or x + dx <= 0 or y + dy > n or y + dy <= 0 or np in area:
			# print(np, area, apples, count)
			break
		#
		if np in apples:
			apples.remove(np)
		else:
			area.popleft()
		# print(np, area, apples, count)
		current = (x + dx, y + dy)
		# check dir
		if turn.get(count):
			direction = (direction + 1) % 4 if turn[count] == "D" else (direction - 1) % 4 
	# print(count)
	return count

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	apples = set()
	turn = dict()
	k = int(sys.stdin.readline().strip())
	for _ in range(k):
		x, y = map(int, sys.stdin.readline().replace('\n', '').split(' '))
		apples.add((x, y))
	l = int(sys.stdin.readline().strip())
	for _ in range(l):
		c, d = sys.stdin.readline().replace('\n', '').split(' ')
		turn[int(c)] = d
	print(solution(n, apples, turn))