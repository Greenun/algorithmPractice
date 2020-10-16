def solution(arr):
    from collections import deque
    divide_line = [(0, 0), (0, 1), (1, 0), (1, 1)]
    queue = deque()
    compressed = list()
    area = ((0, 0), len(arr))
    queue.append(area) # area - (start point, n)
    while queue:
        # print(queue)
        current_st, current_n = queue.popleft()
        cx, cy = current_st
        value = arr[cx][cy]
        if current_n == 1:
            compressed.append((current_st, current_n, value))
            continue
        
        # check
        area = [line[cy:cy+current_n] for line in arr[cx:cx+current_n]]
        if all([row == [value]*current_n for row in area]):
            # compression
            compressed.append((current_st, current_n, value))
        else:
            # divide, add queue
            for i in range(4):
                dx, dy = divide_line[i]
                dx *= (current_n // 2)
                dy *= (current_n // 2)
                queue.append(((cx + dx, cy + dy), current_n // 2))
    answer = [0, 0]
    for cp in compressed:
        _, _, v = cp
        answer[v] += 1
    return answer