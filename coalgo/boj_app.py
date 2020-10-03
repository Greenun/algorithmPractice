import sys
from collections import defaultdict
from copy import deepcopy

def solution(n, m, apps, cost):
	length = sum(cost) + 1
	memory_table = defaultdict(int)
	pool_table = [set() for _ in range(length)]
	pool_table[0] = set(range(len(cost)))
	# reversed_table = defaultdict(int)
	for i in range(length):
		# maximize memory per cost
		# print("i: ", i)
		# print("pt: ", pool_table)
		# print("mt: ", memory_table)
		if not pool_table[i]:
			continue
		# if memory_table[i] < memory_table[i-1]: 
		# 	memory_table[i] = memory_table[i-1]
		# 	pool_table[i] = pool_table[i-1]
		for p in pool_table[i]:
			if i + cost[p] >= length:
				continue
			if memory_table[i+cost[p]] < memory_table[i] + apps[p]:
				# if memory_table[i-1] > memory_table[i] + apps[p]:
				# 	memory_table[i + cost[p]] = memory_table[i-1]
				# 	pool_table[i + cost[p]] = pool_table[i-1]
				# else:
				memory_table[i+cost[p]] = memory_table[i] + apps[p]
				# reversed_table[memory_table[i] + apps[p]] = i + cost[p]
				pool_table[i+cost[p]] = pool_table[i] - {p}
		# print("--------------------")
		# print("pt: ", pool_table)
		# print("mt: ", memory_table)
		# if reversed_table.get(m):
		# 	return reversed_table.get(m)
		# else:
		# 	min_key = float('inf')
		# 	for k in reversed_table.keys():
		# 		if k < m:
		# 			continue
		# 		else:
		# 			if min_key > reversed_table.get(k):
		# 				min_key = reversed_table.get(k)
		# 	if not min_key == float('inf'):
		# 		return min_key
	for i in range(length):
		if memory_table[i] >= m:
			return i
if __name__ == '__main__':
	n, m = map(int, sys.stdin.readline().replace('\n', '').split(' '))
	apps = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	cost = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
	print(solution(n, m, apps, cost))