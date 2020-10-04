import sys

def solution(n, k):
	if k > (n // 2):
		return 0
	table = [[0]*(n+1) for _ in range(k+1)]
	# init
	for i in range(3, n+1):
		table[1][i] = i

	for i in range(2, k+1):
		table[i][i*2] = 2
		for j in range((i*2)+1, n+1):
			table[i][j] = (table[i][j-1] + table[i-1][j-2] ) % 1000000003
	return table[k][n] % 1000000003

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	k = int(sys.stdin.readline().strip())
	print(solution(n, k))