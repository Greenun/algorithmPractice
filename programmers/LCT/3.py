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
	# print(ones, zeros)
	possible = list()
	flag = True if road.startswith('1') else False
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
	# print(possible)
	max_sum = 0
	for p in possible:
		indices = set()
		_sum = 0
		for e in p:
			new_set = {e, e + 1} if flag else {e - 1, e}
			indices = indices.union(new_set)
		
		for i in indices:
			if i < 0 or i >= len(ones):
				continue
			_sum += ones[i]
		_sum += n
		# print(f"sum : {_sum}")
		if max_sum < _sum:
			max_sum = _sum
	return max_sum
		
	# case
	# 0 .. 1 .. 0 : zeros - ones = 1
	#    i1 - 1 ~ in + 1 
	# 1 .. ?(0 or 1) .. 1 : zeros - ones = -1
	#    i1 ~ in + 1
	# 0 .. ? .. 1 : zeros - ones = 0
	# 1 .. ? .. 0 : zeros - ones = 0

if __name__ == '__main__':
	print(solution("111011110011111011111100011111", 3))
	print(solution("001100", 5))
	print(solution("001110111100", 3)) # 10
	print(solution("0011110111110001111111", 3)) # 15
	print(solution("0011110111110001111111", 4)) # 20
	print(solution("1111011111110011101111110", 2)) # 10