def solution(road, n):
	ones, zeros = list(), list()
	zc, oc = 0, 0
	for r in road:
		if r == "1":
			if zc:
				zeros.append(zc)
				zc = 0
			oc += 1
		else:
			if oc:
				ones.append(oc)
				oc = 0
			zc += 1
	if zc:
		zeros.append(zc)
	if oc:
		ones.append(oc)
	print(ones, zeros)
	possible = list()
	if sum(zeros) <= n:
		return len(road)
	for i in range(len(zeros)):
		temp = n
		for j in range(i, len(zeros)):
			if temp - zeros[j] < 0:
				# possible.append(zeros[i:j])
				possible.append(list(range(i,j)))
				break
			elif temp - zeros[j] == 0:
				# possible.append(zeros[i:j+1])
				possible.append(list(range(i,j+1)))
				break
			else:
				temp -= zeros[j]
	flag = True if road.startswith('1') else False
	for p in possible:
		print("p: ", possible)
		if flag:
			pass
			# idx = [x for x in p]
			# idx.append(p[-1] + 1)
			# 0 1 --> 0 (1) 2 (3) 4
		else:
			pass
			# idx = [x - 1 for x in p if not x == 0]
		# print("idx: ", idx)
	

if __name__ == '__main__':
	print(solution("111011110011111011111100011111", 3))
	print(solution("001100", 5))
	print(solution("0011110111110001111111", 3)) # 15
	print(solution("0011110111110001111111", 4)) # 20
	print(solution("1111011111110011101111111", 2)) # 10