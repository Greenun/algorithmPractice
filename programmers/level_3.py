def solution(N, number):
    from collections import defaultdict
    dp = defaultdict(set)
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, (i // 2) + 1):
            prev = dp[i - j]
            curr = dp[j]
            for p in prev:
                for c in curr:
                    # add
                    dp[i].add(c + p)
                    # sub
                    dp[i].add(c - p)
                    dp[i].add(p - c)
                    # mul
                    dp[i].add(c * p)
                    # div
                    if not p == 0:
                        dp[i].add(c // p)
                    if not c == 0:
                        dp[i].add(p // c)
        if number in dp[i]:
            return i
    
    return -1

## 시간 초과
def solution(n, build_frame):
    current = list()
    for build in build_frame:
        current = simulate(current, build)
    
    current = sorted(current, key=lambda c: (c[0], c[1]))
    return current

def simulate(current, action):
    x, y, a, b = action
    prev = [c[:] for c in current]
    if b == 0:
        pass
        # delete
        current.remove([x, y, a])
    else:
        # create
        current.append([x, y, a])
    # print(f"current: {current}, prev: {prev}")
    if check(current):
        return current
    else:
        return prev
    

def check(current):
    # 0 --> y == 0 or on board / pillar
    # 1 --> on pillar / between boards
    # print(current)
    for i in range(len(current)):
        remain = current[:i] + current[i+1:]
        x, y, a = current[i]
        if a == 0:
            if y == 0:
                continue
            else:
                covered = list()
                for rx, ry, ra in remain:
                    if ra == 0:
                        covered.append([rx, ry + 1])
                    else:
                        covered.append([rx, ry])
                        covered.append([rx + 1, ry])
                if not [x, y] in covered:
                    return False
        else:
            pillars, boards = list(), list()
            for r in remain:
                if r[2] == 0:
                    pillars.append(r)
                else:
                    boards.append(r)
            on_pillar = [[pillar[0], pillar[1]+1] for pillar in pillars]
            if [x, y] in on_pillar or [x+1, y] in on_pillar:
                continue
            between = list()
            for board in boards:
                between.append([board[0], board[1]])
                between.append([board[0] + 1, board[1]])            
            if not [x, y] in between or not [x + 1, y] in between:
                return False
            
            # on_pillar = [[pillar[0], pillar[1]+1] for pillar in pillars]
            # if [x, y] in on_pillar or [x + 1, y] in on_pillar:
            #     return True
            # between = list()
            # for board in boards:
            #     between.append([board[0], board[1]])
            #     between.append([board[0] + 1, board[1]])
            # if [x, y] in between and [x + 1, y] in between:
            #     return True
    return True



# < 3000 ms -- 이전의 kakao 5 와 비슷한 시간 - 최대 300 ms 정도 빠름
def solution(n, build_frame):
    current = list()
    for build in build_frame:
        current = simulate(current, build)
    current = sorted(current, key=lambda c: (c[0], c[1], c[2]))
    return current

def simulate(current, action):
    x, y, a, b = action
    prev = [c[:] for c in current]
    
    if b == 0:
        current.remove([x, y, a])        
    else:
        current.append([x, y, a])
    if check(current):
        return current
    else:
        return prev
    
def check(current):
    pillars_covered = list()
    boards_covered = list()
    boards_between = list()
    for cx, cy, ca in current:
        if ca == 0:
            pillars_covered.append([cx, cy + 1])
            boards_covered.append([cx, cy + 1])
        else:
            pillars_covered.append([cx, cy])
            pillars_covered.append([cx + 1, cy])
            boards_between.append([cx, cy])
            boards_between.append([cx + 1, cy])
    for x, y, a in current:
        if a == 0:
            if [x, y] in pillars_covered or y == 0:
                continue
            else:
                return False
        else:
            if [x, y] in boards_covered or [x + 1, y] in boards_covered:
                continue
            if boards_between.count([x, y]) < 2 or boards_between.count([x + 1, y]) < 2:
                return False
    return True
                
    