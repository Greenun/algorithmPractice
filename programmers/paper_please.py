def solution(n, times):
    max_time = max(times)
    upper = max_time * n
    lower = 0
    # time t --> done: (t // all time)
    while lower < upper:
        middle = (lower + upper) // 2
        done = sum([(middle // t) for t in times])
        if done < n:
            lower = middle + 1
        else:
            upper = middle
    # 이 부분 없어도 테스트 통과
    # done = sum([(lower // t) for t in times])
    # while done < n:
    #     lower += 1
    #     done = sum([(lower // t) for t in times])
    return lower