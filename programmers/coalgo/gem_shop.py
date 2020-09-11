def solution(gems):
    from collections import defaultdict
    result = list()
    gems_map = defaultdict(int)
    gems_set = set(gems)

    start, end = 0, 0
    scope_set = set()
    # expand end
    while len(scope_set) < len(gems_set):
        gems_map[gems[end]] += 1
        scope_set.add(gems[end])
        end += 1
    pidx = start
    # shrink start
    while start < len(gems):
        if gems_map[gems[pidx]] <= 0:
            #
            if end >= len(gems): break
            gems_map[gems[end]] += 1
            end += 1
            #
        else:
            result.append([start + 1, end])
            gems_map[gems[start]] -= 1
            pidx = start
            start += 1
    min_idx = 0
    min_value = 1000000
    for i, v in enumerate(result):
        o, t = v
        if min_value > t - o:
            min_idx = i
            min_value = t - o
    return result[min_idx]

