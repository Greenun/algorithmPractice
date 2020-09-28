import sys

def solution(n, s, p):
	origin = list([i % 3 for i in range(n)])
	temp = origin[:]
	shuffle = 0
	answer = p[:]
	# for i in range(n):
	# 	answer[(3*(i//3)) + p[i]] = origin[i]
	
	while temp != answer:
		blanket = temp[:]
		for i in range(n):
			temp[i] = blanket[s[i]]
		shuffle += 1
		if temp == origin:
			return -1
	return shuffle

if __name__ == "__main__":
	n = int(sys.stdin.readline().strip())
	p = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	s = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	print(solution(n, s, p))