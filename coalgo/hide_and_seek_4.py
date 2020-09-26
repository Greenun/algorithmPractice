import sys
from collections import deque

def solution(n, k):
	queue = deque()
	queue.append((n, -1))
	visited = set()
	visited.add(n)
	history = dict()
	count = 0
	while queue:
		temp = deque()
		for _ in range(len(queue)):
			current, prev = queue.popleft()
			history[current] = prev
			if current == k:
				print(count)
				route = get_history(history, k)
				print(' '.join(route))
				return
			next_point = [(np, pp) for np, pp in [(current - 1, current), (current + 1, current), (current*2, current)] if 0 <= np <= 100000]
			for np, prev in next_point:
				if np not in visited:
					temp.append((np, prev))
					visited.add(np)
		queue.extend(temp)
		count += 1

def get_history(history, k):
	current = k
	route = list()
	route.append(str(k))
	while 1:
		value = history.get(current)
		if value == -1:
			break
		route.append(str(value))
		current = value
	return list(reversed(route))

if __name__ == "__main__":
	n, k = map(int, sys.stdin.readline().replace('\n', '').split(' '))
	solution(n, k)