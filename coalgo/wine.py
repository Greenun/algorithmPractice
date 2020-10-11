import sys

def solution(n, wine):
	if n < 3:
		return sum(wine)
	table = [0]*(n+1)
	table[1] = wine[0]
	table[2] = wine[0] + wine[1]
	for i in range(3, n+1):
		table[i] = max(table[i-3] + wine[i-2] + wine[i-1], table[i-2] + wine[i-1], table[i-1])
	return table[n]

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	wine = list()
	for _ in range(n):
		wine.append(int(sys.stdin.readline().strip()))
	print(solution(n, wine))