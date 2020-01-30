import sys

def climb_stairs(l:list):
	dp = [0]*(len(l)+1)
	dp[1] = l[0]
	dp[2] = l[0] + l[1]
	# skipped = False
	# or skipped
	for i in range(3, len(l)+1):
		dp[i] = max(dp[i-3] + l[i-1] + l[i-2], dp[i-2] + l[i-1])
		# if i == len(l):
			# dp[i] = max(dp[i-3]+l[i-1]+l[i-2], dp[i-2]+l[i-1])
			# skipped = False
		# else:
			# dp[i] = max(dp[i-3]+l[i-1]+l[i-2], dp[i-2]+l[i-1], dp[i-1])
			# if dp[i-1] == dp[i]: skipped = True
	print(dp[len(l)])



if __name__ == "__main__":
	climb_stairs([10, 20, 15, 25, 10, 25, 15, 1])
	climb_stairs([1,2,3,4,5,6,7,1])
	'''
	n = int(sys.stdin.readline().strip())
	l = []
	for i in range(0, n):
		l.append(int(sys.stdin.readline().strip()))
	climb_stairs(l)
	'''