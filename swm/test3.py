# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import heapq
N, K = map(int, sys.stdin.readline().replace('\n', '').split(' '))
numbers = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
diff = list()
for i in range(len(numbers)-1):
	d = numbers[i + 1] - numbers[i]
	heapq.heappush(diff, (-1 * d, d))
for _ in range(1, K):
	_ = heapq.heappop(diff)
print(sum([value for _, value in diff]))