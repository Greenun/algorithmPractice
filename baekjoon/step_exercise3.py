import sys

def apartment(k, n):
	_sum = 0
	l = [i+1 for i in range(0, n)]
	for i in range(0, k):
		x = list()
		for m in range(0, n):
			x.append(sum(l[0:m+1]))
		l = x
	print(l[n-1])

def goldbach(n):
	import math
	half = int(n / 2)#n == even num
	a, b = (half, half)
	while 1:		
		check_a, check_b = (False, False)
		
		#check prime
		for i in range(2, int(math.sqrt(a)) + 1):
			if a % i == 0:
				check_a = True
				break
		for i in range(2, int(math.sqrt(b)) + 1):
			if b % i == 0:
				check_b = True
				break
		#
		
		if not check_a and not check_b:
			print(a, b)
			break
		else:		
			a -= 1
			b += 1

def turret(xy1, xy2, r1, r2):
	import math
	if xy1 == xy2 and r1 == r2:
		print(-1)
		return
	x_dist = abs(xy1[0] - xy2[0])
	y_dist = abs(xy1[1] - xy2[1])
	xy_dist = math.sqrt(x_dist**2 + y_dist**2)
	
	rad_sum = r1 + r2
	if xy_dist > rad_sum:
		print(0)
	elif xy_dist == rad_sum:
		print(1)
	else:
		#두 점 사이의 거리가 반지름의 합보다 작은 경우
		#중심이 안 or 밖?
		if r1 > r2:
			if xy_dist > r1:
				#중심이 밖
				print(2)
			elif xy_dist == r1:
				#원 위
				print(2)
			else:
				#원 안
				if xy_dist + r2 > r1:
					print(2)
				elif xy_dist + r2 == r1:
					print(1)
				else:
					print(0)
		else:
			if xy_dist > r2:
				#원 밖
				print(2)
			elif xy_dist == r2:
				#원 위
				print(2)
			else:
				#원 안
				if xy_dist + r1 > r2:
					print(2)
				elif xy_dist + r1 == r2:
					print(1)
				else:
					print(0)


if __name__ == "__main__":
	testcase = int(sys.stdin.readline().strip())
	l = list()
	for i in range(0, testcase):
		values = [int(x) for x in sys.stdin.readline().split(' ')]
		l.append(values)

	for item in l:
		turret(item[0:2], item[3:5], item[2], item[5])
	
	'''l = list()
	for i in range(0, testcase):
		k = int(sys.stdin.readline().strip())
		n = int(sys.stdin.readline().strip())
		l.append([k, n])
	for i in range(0, len(l)):
		apartment(*l[i])
	'''
	'''l = list()
	for i in range(0, testcase):
		n = int(sys.stdin.readline().strip())
		l.append(n)
	for m in l:
		goldbach(m)'''
	

	