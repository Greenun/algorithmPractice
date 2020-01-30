import sys
import copy


def get_fibo(n):
	zero_initial = [1,0,1,1,2,3]
	one_initial = [0,1,1,2,3,5]
	while len(zero_initial) <= n:
		zero_initial.append(zero_initial[len(zero_initial)-1] + zero_initial[len(zero_initial)-2])
	while len(one_initial) <= n:
		one_initial.append(one_initial[len(one_initial)-1] + one_initial[len(one_initial)-2])
	print(zero_initial[n], one_initial[n])

def fibonacci(n):
	if n == 0:
		print("0")
		return 0
	elif n == 1:
		print("1")
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)


def make_one(n):
	init_make = [-1,0,1,1,2]
	if n <= 4:
		print(init_make[n])
		return
	init_make.extend([-1]*(n-3))

	for i in range(5, n+1):
		if i % 6 == 0:
			init_make[i] = min(init_make[int(i/3)], init_make[int(i/2)], init_make[i-1]) + 1
		elif i % 3 == 0:
			init_make[i] = min(init_make[int(i/3)], init_make[i-1]) + 1
		elif i % 2 == 0:
			init_make[i] = min(init_make[int(i/2)], init_make[i-1]) + 1
		else:
			init_make[i] = init_make[i-1] + 1
	print(init_make[n])

def wine(l):
	seq = all_seq(len(l))
	b = []
	for m in seq:
		b.append(get_sum(l, m))
	print(max(b))

def get_sum(l, seq):
	_sum = 0
	for i, c in enumerate(seq):
		if c == '1':
			_sum += l[i]
	return _sum

def get_seq(s:str):
	es1 = s + '0'
	es2 = s + '1'
	ret = []
	if es1.find('111') == -1:
		ret.append(es1)
	if es2.find('111') == -1:
		ret.append(es2)
	return ret

def all_seq(n:int):
	import time
	l = ['0', '1']
	cnt = 1
	temp = []
	prev = 0
	now = len(temp)
	while cnt < n:
		for i in l:
			t = get_seq(i)
			temp.extend(t)
		now = len(temp)
		l = temp[prev:now]
		prev = len(temp)
		cnt += 1

	return l

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	l = []
	for i in range(0, n):
		l.append(int(sys.stdin.readline()))
	wine(l)
	'''
	t = int(sys.stdin.readline())
	l = []
	for i in range(0, t):
		n = int(sys.stdin.readline())
		l.append(n)
	for i in l:
		get_fibo(i)
	'''