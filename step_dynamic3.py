import sys

def packing(k, w, v):
	#d = [0]*(k+1)
	d = [0]
	d.extend([-1]*k)
	d_seq = [[] for x in range(k+1)]
	for i in range(1, k+1):
		temp = []
		temp_seq = []
		for idx, j in enumerate(w):
			if i-j < 0:
				continue
			else:
				if idx in d_seq[i-j]:
					#print(i, idx, d_seq[i-j])
					continue
				else:
					temp.append(d[i-j] + v[idx])
					t = d_seq[i-j][:]
					t.append(idx)
					temp_seq.append(t)
		m = max(temp) if temp else d[i-1]
		d[i] =  m if m > d[i-1] else d[i-1]
		if d[i] == d[i-1]:
			d_seq[i] = d_seq[i-1]
		else:
			d_seq[i] = temp_seq[temp.index(m)] if temp else d_seq[i-1]
	print(d)

def packing2(k, w, v):
	d = [0]*(k+1)
	for i in range(0, len(w)):
		for j in range(k, 0, -1):
			if j - w[i] < 0:
				pass
			else:
				d[j] = max(d[j], d[j-w[i]] + v[i], d[j-1])
	print(d[k])

if __name__ == '__main__':
	n, k = map(int, sys.stdin.readline().replace('\n', '').split(' '))
	w = []
	v = []
	for i in range(0, n):
		a, b = map(int, sys.stdin.readline().replace('\n', '').split(' '))
		w.append(a)
		v.append(b)
	packing(k, w, v)

	
	#packing2(50, [6,4,3,5,1], [13, 8, 6, 12, 3])
	#packing2(7, [6,4,3,5], [13, 8, 6, 12])
	'''packing(20, [2,2,6,7], [3,5,12,14])
	packing(17, [1,5,2,5], [6,0,1,4])
	packing(20, [1,7,4,2], [2, 25, 6, 3])
	packing(31, [3,7,4,2,15], [4,9,9,8,150])
	'''