import sys
import math

def alpha_centauri(x, y):
	dist = y - x
	_max = int(math.sqrt(dist))
	interval = dist - _max**2

	base = ( _max * 2 )- 1
	offset = math.ceil(interval / _max)

	print(base + offset)

def snail(a,b,v):
	base = v - a

	print(math.ceil( base / (a-b) ) + 1)

def hotel(h, w, n):
	num = math.ceil(n / h)
	floor = n % h
	floor = h if floor == 0 else floor

	h_digit = len(str(h))
	w_digit = 2
	
	num = str(num).zfill(w_digit)

	print(str(floor) + num)


if __name__ == '__main__':
	test_case = int(sys.stdin.readline().strip())
	whole_cases = list()

	for i in range(0, test_case):
		whole_cases.append([int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')])
	for case in whole_cases:
		hotel(*case)
	'''test_case = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
	snail(*test_case)'''

	'''test_case = int(sys.stdin.readline().strip())
	whole_cases = list()
	for i in range(0, test_case):
		cases = sys.stdin.readline().replace('\n', '').split(' ')
		cases = [int(x) for x in cases]
		whole_cases.append(cases)

	for cases in whole_cases:
		alpha_centauri(*cases)'''


