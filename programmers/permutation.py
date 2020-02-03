def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n)) # current permutation
    cycles = list(range(n, n-r, -1))
    # print(indices, cycles)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            print(i, indices, cycles)
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    count = 1
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
        count += 1
        print(f"count: {count}\nc: {c}\ni: {i}\narr: {arr}\n")
        # print(f'c: {c} arr: {arr}')
    return result

if __name__ == '__main__':
	# print(permute(['A','B','C']))
	for i in permutations(['A', 'B', 'C'], 3):
		pass