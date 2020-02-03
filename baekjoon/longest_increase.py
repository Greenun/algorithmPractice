import sys

def lis(l):
	dp = [1]*len(l)
	for i in range(0, len(l)):
		for j in range(0, i):
			if l[i] > l[j]:
				dp[i] = max(dp[i], dp[j]+1)
	print(dp)
	#print(dp[len(l)-1])
	print(max(dp))
		

	# m = []
	# for i in range(0, len(l)):
	# 	subseq = l[i:]
	# 	temp = [subseq[0]]
	# 	for s in subseq:
	# 		if temp[len(temp)-1] < s:
	# 			temp.append(s)
	# 		else:
	# 			continue
	# 	if len(temp) > len(m):
	# 		m = temp
	# 	print(temp)
	# print(m, len(m))

if __name__ == "__main__":
	# lis([10, 20, 10, 30, 20, 50])
	lis([10, 20, 15, 30 ,20, 25])
	# lis([4, 1, 2, 5, 3, 7, 8, 10])
	# lis([2,3,4,1,5,7,6])
	lis([10,8,6,4,2])
	'''
	n = int(sys.stdin.readline().strip())
	l = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	lis(l)
	'''