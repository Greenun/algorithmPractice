# 중복 X, 순서 O - permutations
def solution(user_id, banned_id):
    from collections import defaultdict
    visited = defaultdict(set)
    cases = list()
    for bid in banned_id:
        temp = list()
        for uid in user_id:
            if get_match(uid, bid):
                temp.append(uid)
        cases.append(temp)
    print(cases)
    total = list()
    track(cases, [], [], total)    
    
def get_match(uid, bid):
    match = False
    if not len(uid) == len(bid):
        return match
    for i in range(len(bid)):
        if bid[i] == '*' or uid[i] == bid[i]:
            match = True
        else:
            match = False
            break
    return match

def track(cases, visited, result, total):
    if not cases:
        total.append(result[:])
        return
    case = cases[0]
    for uid in case:
        if uid not in visited:
            visited.append(uid)
            result.append(uid)
            track(cases[1:], visited[:], result, total)           
            result.pop()
            visited.pop()

# permutation 후 중복 제거
def solution(user_id, banned_id):
    from collections import defaultdict
    visited = defaultdict(set)
    cases = list()
    for bid in banned_id:
        temp = list()
        for uid in user_id:
            if get_match(uid, bid):
                temp.append(uid)
        cases.append(temp)
    total = list()
    track(cases, [], [], total)
    total_set = list()
    for t in total:
        temp = set()
        for x in t:
            temp.add(x)
        if temp not in total_set:
            total_set.append(temp)
    return len(total_set)
    
def get_match(uid, bid):
    match = False
    if not len(uid) == len(bid):
        return match
    for i in range(len(bid)):
        if bid[i] == '*' or uid[i] == bid[i]:
            match = True
        else:
            match = False
            break
    return match

def track(cases, visited, result, total):
    if not cases:
        total.append(result[:])
        return
    case = cases[0]
    for uid in case:
        if uid not in visited:
            visited.append(uid)
            result.append(uid)
            track(cases[1:], visited[:], result, total)           
            result.pop()
            visited.pop()