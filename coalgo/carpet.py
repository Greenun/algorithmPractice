def solution(brown, yellow):
    import math
    area = brown + yellow
    ables = list()
    for i in range(1, int(math.sqrt(area)) + 1):
        if area % i == 0:
            ables.append((area // i, i))
    for a in ables:
        w, h = a
        if brown == 2*(w + h) - 4:
            return a
