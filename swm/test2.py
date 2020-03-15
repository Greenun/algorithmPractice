# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def check(tile, point):
	i, j = point
	n, m = (len(tile), len(tile[0]))
	check_points = [ [(i, j + 1), (i + 1, j + 1), (i + 1, j)], 
									[(i, j - 1), (i + 1, j - 1), (i + 1, j)], 
									[(i, j + 1), (i - 1, j), (i - 1, j + 1)], 
									[(i, j - 1), (i - 1, j - 1), (i - 1, j)] 
								 ]	
	for check_point in check_points:
		temp = 0
		for cp in check_point:
			x, y = cp
			if x < 0 or x > n - 1 or y < 0 or y > m - 1:
				continue
			if tile[x][y] == '1':
				temp += 1
		if temp >= 3:
			return True
	return False

import sys
T = int(sys.stdin.readline().replace('\n', ''))
temp = list()
for _ in range(T):
	n, m = map(int, sys.stdin.readline().replace('\n', '').split(' '))
	tile = list()
	for _ in range(n):
		line = sys.stdin.readline().replace('\n', '').split(' ')
		tile.append(line)
	temp.append(tile)
for tile in temp:
	ret = True
	for i, line in enumerate(tile):
		for j, t in enumerate(line):
			if t == '1':
				if not check(tile, (i, j)):
					ret = False
					break
			else:
				continue
	stdout = "YES" if ret else "NO"
	print(stdout)