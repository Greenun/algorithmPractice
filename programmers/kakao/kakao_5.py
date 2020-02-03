def solution(n, build_frame):
    answer = []
    current = []
    for build in build_frame:
        points = build[0:2]
        spec = build[2] # 0: pillar, 1: beam
        work = build[3] # 0: delete, 1: create
        current, result = simulate(n, current, points, spec, work)
    answer = current
    print('answer: ', answer)
    return answer

def simulate(n, current, points, spec, work):
    # print(current)
    copies = [list(c) for c in current] if current else []
    print('target: ', points+[spec])
    # add
    if work == 1:
        copies.append(points + [spec])
    else:        
        # delete
        copies.remove(points + [spec])
    if check_rules(copies, n):
        return copies, True
    else:
        return current, False
    
def check_rules(current, n):
    
    # if len(current) < 2: return True
    floors = [[k, 0] for k in range(n+1)]
    beams = [[c[0], c[1]] for c in current if c[2] == 1]
    pillars = [[c[0], c[1]] for c in current if c[2] == 0]

    print('beams:', beams)
    print('pillars:',pillars)
    on_pillars = [[p[0], p[1] + 1] for p in pillars]
    print('on_pillars:', on_pillars)
    for beam in beams:
        # check is between beams
        if ([beam[0] - 1, beam[1]] in beams) and ([beam[0] + 1, beam[1]] in beams):
            continue
        elif (beam in on_pillars) or ([beam[0]+1, beam[1]] in on_pillars):
            continue
        else:
            return False
    beam_ends = [[b[0] + 1, b[1]] for b in beams]
    for pillar in pillars:
        if pillar in beam_ends:
            continue
        elif pillar in on_pillars:
            continue
        elif pillar in floors:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
