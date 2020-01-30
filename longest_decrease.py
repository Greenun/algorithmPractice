import sys

def lds(l):
	dp = [1]*len(l)
	for i in range(0, len(l)):
		for j in range(0, i):
			if l[i] < l[j]:
				dp[i] = max(dp[i], dp[j]+1)
	print(max(dp))

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	l = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	lds(l)