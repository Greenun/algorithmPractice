def solution(a):
    n = len(a)
    poss = set()
    lm = [0]*n
    rm = [0]*n
    l_min = float('inf')
    r_min = float('inf')
    for i in range(n):
        if l_min > a[i]:
            l_min = a[i]
        lm[i] = l_min
        if r_min > a[n-1-i]:
            r_min = a[n-1-i]
        rm[n-1-i] = r_min
    count = 2
    for i in range(1, n - 1):
        if lm[i-1] < a[i] and rm[i+1] < a[i]:
            continue
        else:
            count += 1
    return count
    