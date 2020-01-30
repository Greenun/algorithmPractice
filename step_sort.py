import sys
import math
import time

def binary_search(l, num):
	mid = int((len(l) - 1 )/ 2)
	low = 0
	high = len(l) - 1
	while 1:
		if high - low <= 1:
			break
		#mid = int((low + high) / 2)
		mid = int((low + high) / 2)
		print(low, mid, high)
		if l[mid] < num:
			#mid = int((low + high) / 2) 
			low = mid
		else:
			#mid = int((low + high) / 2) 
			high = mid
		time.sleep(1)
	mid = int((low + high) / 2)
	if l[len(l)-1] <= num:
		mid = high + 1
	elif l[0] > num:
		mid = 0
	else:
		mid += 1
		
		
	print(mid)
	l.insert(mid, num)
	print(l)

def search_index(l, num):
	#mid = 0
	if l[len(l) - 1] < num:
		mid = len(l)
	elif l[0] > num:
		mid = 0
	else:
		high = len(l) - 1
		low = 0
		while 1:
			if high - low <= 1: break
			mid = int((low + high) / 2)
			if l[mid] < num:
				low = mid
			else:
				high = mid
		mid = int((low + high) / 2)
		mid += 1
	l.insert(mid, num)
	return l

'''if __name__ == "__main__":
	n = int(sys.stdin.readline())
	l = [0] * 10001
	for i in range(0, n):
		num = int(sys.stdin.readline())
		l[num] += 1
	cnt = 0
	for i in range(0, len(l)):
		if cnt >= n: break
		if l[i] > 0:
			for m in range(0, l[i]):
				print(i)
				cnt += 1'''
def statistics(l):
	avg = sum(l) / len(l)
	if (avg*2).is_integer():
		avg = math.ceil(avg)
	else:
		avg = round(avg)
	print(avg)
	#
	srtd = merge_sort(l)
	#print(srtd)
	median = srtd[int(len(srtd) / 2)]
	print(median)

	#
	count = [0]*8001#-4000 ~ 4000
	for e in srtd:
		count[e+4000] += 1
	m = max(count)
	if count.count(m) >= 2:
		temp = [i for i, f in enumerate(count) if f == m]
		print(temp[1] - 4000)
	else:
		print(count.index(m) - 4000)
	#
	scope = srtd[len(srtd)-1] - srtd[0]
	print(scope)


def merge_sort(l):
	if len(l) == 1:
		return l
	else:
		m = l[0:math.ceil(len(l)/2)]
		n = l[math.ceil(len(l)/2):len(l)]
		#print(m, n)
		m = merge_sort(m)
		n = merge_sort(n)
		merged = merge(m, n)
		return merged

def merge(m, n):
	merged = []
	lenm = len(m)
	lenn = len(n)
	mdx = 0
	ndx = 0
	while not (mdx == lenm or ndx == lenn):
		if m[mdx] >= n[ndx]:
			merged.append(n[ndx])
			ndx += 1
		else:
			merged.append(m[mdx])
			mdx += 1
	
	if mdx == lenm:
		while ndx != lenn:
			merged.append(n[ndx])
			ndx += 1
	elif ndx == lenn:
		while mdx != lenm:
			merged.append(m[mdx])
			mdx += 1
	return merged

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	l = []
	for i in range(0, n):
		m = int(sys.stdin.readline())
		l.append(m)
	statistics(l)
