import sys
from collections import defaultdict

def solution(n, m, oracles, parties):
	party_groups = defaultdict(set)
	idx = 0
	for i, party in enumerate(parties):
		party_groups[i] = party

	for _ in range(m):
		for party in parties:
			keys = party_groups.keys()
			for k in keys:
				if party_groups[k].intersection(party):
					party_groups[k] = party_groups[k].union(party)		
	count = 0
	for k in party_groups:
		if not oracles.intersection(party_groups[k]):
			count += 1
	return count

if __name__ == '__main__':
	n, m = map(int, sys.stdin.readline().replace("\n", "").split(' '))
	oracles = list()
	second_input = list(map(int, sys.stdin.readline().replace("\n", "").split(' ')))
	if len(second_input) > 1:
		oracles = set(second_input[1:])
	else:
		oracles = set()
	parties = list()
	for _ in range(m):
		nth_input = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
		if len(nth_input) > 1:
			nth_input = nth_input[1:]
		parties.append(set(nth_input))
	print(solution(n, m, oracles, parties))

# 6 5
# 1 6
# 2 4 5
# 2 1 2
# 2 2 3
# 2 3 4
# 2 5 6

# 5 3
# 1 3
# 3 1 2 4
# 3 1 4 5
# 1 3