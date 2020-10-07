import sys

def solution(k, pages):
	table = [[float('inf')]*k for _ in range(k)]
	for i in range(k):
		table[i][i] = 0
# 15
# 1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
	for i in range(k):
		for j in range(i, k):
			left = j - i
			s = sum(pages[left:j+1])
			for d in range(left, j):
				mid = d
				# print(left, mid, j)
				# print_table(table)
				table[left][j] = min(table[left][j], table[left][mid] + table[mid+1][j] + s) 
	print(table)
	return table[0][k-1] # + sum(pages)
# def print_table(table):
# 	for line in table:
# 		print(line)

if __name__ == '__main__':
	t = int(sys.stdin.readline().strip())
	for _ in range(t):
		k = int(sys.stdin.readline().strip())
		pages = (list(map(int, sys.stdin.readline().replace('\n', '').split(' '))))
		print(solution(k, pages))