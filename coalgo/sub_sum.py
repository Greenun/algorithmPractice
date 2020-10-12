import sys

def solution(n, s, numbers):
	left = 0
	right = 0
	minimum = n + 1
	_sum = numbers[0]
	while left <= right:
		if _sum < s:
			# expand
			right += 1
			if right >= n:
				break
			_sum += numbers[right]
		else:
			# shrink
			if minimum > right - left + 1 and right - left + 1 > 0:
				minimum = right - left + 1
			_sum -= numbers[left]
			left += 1
	return minimum if not minimum == n + 1 else 0

if __name__ == '__main__':
	n, s = list(map(int, sys.stdin.readline().replace('\n', '').split()))
	numbers = list(map(int, sys.stdin.readline().replace('\n', '').split()))
	print(solution(n, s, numbers))


		# while left < n - 1 and _sum >= s:
			# 	left += 1
			# 	_sum -= numbers[left]
			# 	if _sum >= s and minimum > right - left:
			# 		minimum = right - left