def solution(dartResult):
    bonus = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    options = {
        '*': 2,
        '#': -1
    }
    score_queue = list()
    word = ""
    score = 0
    for c in dartResult:
        if c.isdigit():
            word += c
        elif bonus.get(c):
            print(word)
            score_queue.append(int(word))
            word = ""
            score_queue[-1] = score_queue[-1]**bonus.get(c)
        elif c == "*" and len(score_queue) > 1:
            score_queue[-1] = score_queue[-1]*options.get(c)
            score_queue[-2] = score_queue[-2]*options.get(c)
        else:
            score_queue[-1] = score_queue[-1]*options.get(c)
    return sum(score_queue)
    
