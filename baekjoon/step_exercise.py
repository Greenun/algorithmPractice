#1 -> 2 / 2 -> 4 / 3 -> 6.. 
#10 -> 11 / 11 -> 13 / 12 -> 15 / 13 -> 17 / 14 -> 19
#20 -> 22 / 21 -> 24 / 22 -> 26 / 23 -> 28 ..
#30 -> 33 / 31 -> 35 .. 39 -> 51
#40 -> 44 ..
#100 -> 101 / 101 -> 103 /  102 -> 105 / 103 -> 107 / 104 -> 109 / 105 -> 111 / 109 -> 119 / 110 -> 112
#200 -> 202 / 201 -> 204
import sys

def self_number():
	numbers = list(range(0, 10001))

	for i in range(0, 9999):
		try:
			n = i
			s = str(i)
			for m in s:
				n += int(m)
			numbers.remove(n)
		except ValueError:
			pass
	for el in numbers:
		print(el)


def hansu(n):
	cnt = 0
	for i in range(1, n+1):
		s = str(i)
		prev = -10
		if len(s) <= 2:
			cnt += 1
			continue
		for m in range(0, len(s) - 1):
			if prev != int(s[m+1]) - int(s[m]):
				if m == 0:
					pass
				else:
					cnt -= 1
					break
			prev = int(s[m+1]) - int(s[m])
		cnt += 1
	print(cnt)

def factorial(n):
	mul = 1
	for i in range(1, n+1):
		mul *= i
	print(mul)

def hanoi(n, frm, to, tmp):
	#cnt = 2**n - 1
	#towers = [list(range(1, n+1)), [], []]
	#moves = list()
	
	if n == 1:
		print("%d %d" % (frm, to))
		return
	#frm to tmp 1 3 2
	hanoi(n-1, frm, tmp, to)
	print("%d %d" % (frm, to))
	hanoi(n-1, tmp, to, frm)

def break_even(a, b, c):
	cost = a
	if b >= c:
		print(-1)
		return
	import math
	cnt = math.ceil(a / (c-b)) if not a % (c-b) == 0 else int(a / (c-b)) + 1
	print(cnt)

def salt_delivery(n):
	if n % 5 == 0:
		cnt = int(n / 5)
	elif n % 5 == 1:
		if (n / 5) < 1: cnt = -1
		else: cnt = int(n / 5) + 1# - 1 + (6 / 3)
	elif n % 5 == 2:
		if (n / 5) < 2: cnt = -1
		else: cnt = int(n / 5) + 2# - 2 + (12 / 3)
	elif n % 5 == 3:
		cnt = int(n / 5) + 1
	else:
		if (n / 5) < 1: cnt = -1
		else: cnt = int(n / 5) + 2# - 1 + ( 9 / 3 )
	print(cnt)

def bee_house(x):
	import math
	n = int(math.sqrt(x) / 2)
	hae = 0.5 + math.sqrt(12*x - 3) / 6
	print(math.ceil(hae))
	
	'''while 1:
		if an < x and x <= an + 6*n:
			n += 1
			break
		an += 6*n
		n += 1'''
	#print(n)

def find_fraction(x):
	import math
	n = math.sqrt(2*x + 1/4) - 1 / 2
	n = math.ceil(n)
	prev = int(n*(n-1) / 2)
	current = x - prev

	answer = None
	if n % 2 == 0: 
		answer = str(current) + "/" + str(n - current + 1)
	else:
		answer = str(n - current + 1) + "/" + str(current)
	print(answer)

if __name__ == '__main__':
	x = sys.stdin.readline().strip()
	find_fraction(int(x))
	#x = sys.stdin.readline().strip()
	#bee_house(int(x))
	#n = sys.stdin.readline().strip()
	#salt_delivery(int(n))
	#a, b, c = sys.stdin.readline().split(" ")
	#break_even(int(a), int(b), int(c.strip()))

