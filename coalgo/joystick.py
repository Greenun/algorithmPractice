# 문제 이상함.. 더 알아보는중..
def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    changes = list()
    n = len(name)
    for i, c in enumerate(name):
        if not c == "A":
            idx = alphabet.index(c)
            if idx > 13:
                idx = 26 - idx
            count += idx
            changes.append(i)
    current = 0
    current_v = 0
    if changes and changes[0] != 0:
        changes.insert(0, 0)
    # print(changes)
    while len(changes) > 1:
        left = changes[current - 1]
        right = changes[current + 1]
        left_gap = n - left + current_v if left > current_v else current_v - left
        right_gap = n - current_v + right if right < current_v else abs(current_v - right)
        # print(current_v, changes, left, right, left_gap, right_gap)
        if right_gap <= left_gap:
            changes.pop(current)
            current = 0
            current_v = right
            count += right_gap
        else:
            changes.pop(current)
            current = -1
            current_v = left
            count += left_gap
    
    return count
