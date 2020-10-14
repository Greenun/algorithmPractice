import sys

def solution(n, matrixes):
	table = [[float('inf')]*n for _ in range(n)]
	matrix_table =  [[0]*n for _ in range(n)]
	for i in range(n):
		table[i][i] = 0
		matrix_table[i][i] = matrixes[i]

	for d in range(1, n):
		for x in range(n - d):
			y = x + d
			for m in range(x, y):
				lr, lc = matrix_table[x][m]
				rr, rc = matrix_table[m+1][y]
				if table[x][y] > table[x][m] + table[m+1][y] + lr*rr*rc:
					table[x][y] = table[x][m] + table[m+1][y] + lr*rr*rc
					matrix_table[x][y] = (lr, rc)
	return table[0][n-1]

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	matrix_list = list()
	for _ in range(n):
		matrix_list.append(tuple(map(int, sys.stdin.readline().replace("\n", "").split(" "))))
	print(solution(n, matrix_list))