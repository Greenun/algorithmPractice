import sys
import copy

def blackjack(original: list, m: int):
	number_couples = list()
	less_than_m = list()
	for i in range(0, len(original)):
		for j in range(i+1, len(original)):
			if original[i] + original[j] <= m:
				number_couples.append((original[i], original[j]))
	
	for n in number_couples:
		temp = copy.deepcopy(original)
		temp.remove(n[0])
		temp.remove(n[1])
		
		for i in temp:
			if sum(n) + i == m:
				
				print(m)
				return
			elif sum(n) + i < m:
				less_than_m.append(sum(n) + i)
	
	print(max(less_than_m))

if __name__=='__main__':
	n, m = [int(x) for x in sys.stdin.readline().replace("\n", "").split(' ')]
	original = [int(x) for x in sys.stdin.readline().replace("\n", "").split(' ')]


	blackjack(original, m)
