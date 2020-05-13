# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# N개의 점(s1, e1)에 대해서 각 점이 다른 모든 점(s2, e2) s2 < s1 < e2 를 만족하는 갯수
import sys
n = int(sys.stdin.readline().replace('\n', ''))
participants = list()
for _ in range(n):
	participants.append(list(map(int, sys.stdin.readline().replace('\n', '').split(' '))))

# not efficient..T_T
for i in range(len(participants)):
	count = 0
	ps, pe = participants[i]
	for v in participants[:i] + participants[i+1:]:
		s, e = v
		if ps > s and ps < e:
			count += 1
	print(count)

# (x1, y1) (x2, y2) ... (xn, yn)
# x를 기준으로 tree를 구성 --> 조건에 맞으면 y값을 비교
# tree --> nlogn / compare --> n^2 / 2
# 흠.. 더 좋은 방법은..?
