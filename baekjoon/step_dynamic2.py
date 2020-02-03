import sys

'''def continuous_sum(l):
	_sum = 0
	_max = float('-inf')
	store = []
	for i in l:
		_sum += i
		if _sum > _max:
			store.append(_sum)
			_max = _sum
		if _sum < 0:
			_sum = 0

	print(max(store))
'''
#dp version
def continuous_sum(l):
	d = [float('-inf'), l[0]]
	d.extend([float('-inf')]*(len(l)))
	idx = 2
	for i in l[1:]:
		d[idx] = max(d[idx-1]+i, i)
		idx += 1
	print(max(d))

'''
def coin_theory(l, k):
	d = [0]
	d_current = [0]*(k+1)
	_max = l[len(l)-1]
	for i in range(1, k+1):
		if i % _max == 0:
			d_current[i] += 1
	d_prev = d_current[:]
	for i in reversed(range(0, len(l)-1)):
		d_current = [0]*(k+1)
		d_current[l[i]] += 1
		for m in range(l[i]+1, k+1):
			d_current[m] = d_current[m-l[i]] + d_prev[m]
		d_prev = d_current[:]
	print(d_current[k])
'''

def coin_theory(l, k):
	d = [1]
	d.extend([0]*k)
	for i in l:
		for m in range(i, k+1):
			d[m] = d[m-i] + d[m]
	print(d[k])



if __name__ == "__main__":
	n, k = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
	l = []
	for i in range(0, n):
		num = int(sys.stdin.readline())
		l.append(num)
	coin_theory(l, k)
	'''dp = [0 for i in range(k+1)]
	dp[0] = 1
	for i in l:
	    for j in range(i, k+1):
	        dp[j] += dp[j-i]
	print(dp[k])'''
	'''
	n = int(sys.stdin.readline())
	l = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
	continuous_sum(l)
	'''
	'''continuous_sum([10, -4, 3, 1, 5, 6, -35, 12, 21, -1])
	continuous_sum([500, 100, -300, -400, 100, 10, 1])
	continuous_sum([-1,-2,-3])'''