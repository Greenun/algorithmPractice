import sys

def solution(n, heights):
	buildings = [(i+1, height) for i, height in enumerate(heights)]
	views = [0]*n
	for i in range(n):
		cx, cy = buildings[i]
		max_gradient = float('-inf')
		for j in range(i+1, n):
			if i == j: continue
			x, y = buildings[j]
			gradient = (cy - y) / (cx - x) if cx - x != 0 else 0
			if max_gradient < gradient:
				views[i] += 1
				views[j] += 1
				max_gradient = gradient
	return max(views)

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	heights = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	print(solution(n, heights))

# 첫 풀이 - 마지막 부분에서 틀림 - 부동소수점 오차로 틀린 것으로 추정중..
# def find_view(buildings, n, k):
# 	ix, iy = buildings[k]
# 	left = k - 2
# 	right = k + 2
# 	count = 1 if k == 0 or k == n - 1 else 2
# 	while left >= 0 or right < n:
# 		if left >= 0:
# 			lx, ly = buildings[left]
# 			a = (iy - ly) / (ix - lx) if ix - lx != 0 else 0
# 			b = iy - a*ix
			
# 			left_check = lambda x, y: y < a*x + b
# 			if all([left_check(x, y) for x, y in buildings[lx:ix-1]]):
# 				count += 1
# 			left -= 1
# 		if right < n:
# 			rx, ry = buildings[right]
# 			a = (iy - ry) / (ix - rx) if ix - rx != 0 else 0
# 			b = iy - a*ix
			
# 			right_check = lambda x, y: y < a*x + b 
# 			if all([right_check(x, y) for x, y in buildings[ix:rx-1]]):
# 				count += 1
# 			right += 1
# 	return count