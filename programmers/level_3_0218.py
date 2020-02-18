# failed...
def solution(key, lock):
    m = len(key)
    n = len(lock)
    extended_lock = [[0]*(2*(n - 1) + m) for _ in range(2*(n - 1) + m)]
    for i in range(m):
        for j in range(m):
            extended_lock[n - 1 + i][n - 1 + j] = lock[i][j]
    for k in rotate(key):
        print('-------------')
        # down
        for i in range(n + m - 1):
            # right
            for j in range(n + m - 1):
                temp = [el[:] for el in extended_lock]
                for r in range(n):
                    for c in range(n):
                        temp[r + i][c + j] += key[r][c]
                if check(temp, n, m):
                    return True
    return False

def rotate(key):
    n = len(key)
    r_90 = [list() for _ in range(n)]
    for i in range(n):
        for j in range(n-1, -1, -1):
            r_90[i].append(key[j][i])
    r_180 = [key[i][::-1] for i in range(len(key)-1, -1, -1)]
    r_270 = [list() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            r_270[i].append(key[j][-1*(i+1)])
    return [key, r_90, r_180, r_270]

def check(e_lock, n, m):
    print(e_lock)
    for i in range(m):
        for j in range(m):
            if not e_lock[n - 1 + i][n - 1 + j] == 1:
                return False
    return True

# 다시 한 풀이
def solution(key, lock):
    m = len(key)
    n = len(lock)
    extended_lock = [[0]*(2*(m - 1) + n) for _ in range(2*(m - 1) + n)]
    for i in range(n):
        for j in range(n):
            extended_lock[m - 1 + i][m - 1 + j] = lock[i][j]
    for k in rotate(key):
        # down
        for i in range(n + m - 1):
            # right
            for j in range(n + m - 1):
                temp = [el[:] for el in extended_lock]
                for r in range(m):
                    for c in range(m):
                        temp[r + i][c + j] += k[r][c]
                if check(temp, n, m):
                    return True
    return False

def rotate(key):
    n = len(key)
    r_90 = [list() for _ in range(n)]
    for i in range(n):
        for j in range(n-1, -1, -1):
            r_90[i].append(key[j][i])
    r_180 = [key[i][::-1] for i in range(len(key)-1, -1, -1)]
    r_270 = [list() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            r_270[i].append(key[j][n - 1 - i])
    return [key, r_90, r_180, r_270]

def check(e_lock, n, m):
    for i in range(n):
        for j in range(n):
            if not e_lock[m - 1 + i][m - 1 + j] == 1:
                return False
    return True

def solution(operations):
    import heapq
    min_queue, max_queue = list(), list()
    length = 0
    for operation in operations:        
        action, number = operation.split(' ')
        number = int(number)
        if action == "I":
            heapq.heappush(min_queue, number)
            heapq.heappush(max_queue, -1*number)
            length += 1
        else:
            if length == 0:
                continue
            if number == 1:
                value = heapq.heappop(max_queue)
            else:
                value = heapq.heappop(min_queue)
            length -= 1
            if length == 0:
                # D 연산에 의해 queue 길이가 0 일 경우 min, max queue의 싱크가
                # 안 맞아서 다른 값이 나올 수 있다.
                min_queue, max_queue = list(), list()
    if length == 0:
        return [0, 0]
    else:
        min_v = heapq.heappop(min_queue)
        max_v = heapq.heappop(max_queue) * -1
        return [max_v, min_v]