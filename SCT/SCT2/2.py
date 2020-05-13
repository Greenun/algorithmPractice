# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# pair로 모든 인원의 관계를 구하고 해당 pair(의 능력치 좌표)를 포함하는 가장 큰 직사각형의 둘레
import sys
from collections import defaultdict

def subset_check(temp, teams):
	for team in teams:
		if temp.issubset(team):
			return True
	return False

def get_rectangle(team, status):
	x_list, y_list = list(), list()
	for t in team:
		x, y = map(int, status[int(t) - 1])
		x_list.append(x)
		y_list.append(y)
	return ((max(x_list) - min(x_list)) + (max(y_list) - min(y_list))) * 2
	

n, m = map(int, sys.stdin.readline().replace('\n', '').split(' '))
status = list()
teams = list()
relations = defaultdict(set)
for _ in range(n):
	status.append(sys.stdin.readline().replace('\n', '').split(' '))
for _ in range(m):
	x, y = sys.stdin.readline().replace('\n', '').split(' ')
	relations[x].add(y)
	relations[y].add(x)
for k in relations:
	temp = set(k)
	for v in relations[k]:
		temp = temp.union(relations[v])
	if not subset_check(temp, teams):
		teams.append(temp)
max_status = 0
for team in teams:
	per = get_rectangle(team, status)
	if  per > max_status:
		max_status = per
print(max_status)