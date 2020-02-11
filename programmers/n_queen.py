# non-recursive --> 시간 초과
# check 수정하여 시간 맞춤
def solution(n):
    count = 0
    row = 0
    col = 0
    temp = list()
    while 1:
        if row == 0 and col == n:
            break
        while col < n:
            if check(temp, row, col):
                temp.append(col)
                row += 1
                col = 0
            else:
                col += 1
        if row == n or col == n:
            # backtrack
            if row == n:
                count += 1
            if len(temp) == 0:
                continue
            else:
                col = temp.pop() + 1
                row -= 1
    return count

def check(current, row, col):
    # restricted = list()
    # for i, c in enumerate(current):
    #     restricted.extend([c + row - i, c - row + i, c])
    # if col in restricted:
    #     return False
    # return True
    for i, c in enumerate(current):
        if c == col or (c + row - i) == col or (c - row + i ) == col:
            return False
    return True
            

# recursive ver

def solution(n):
    current = list()
    count = 0
    temp, count = backtrack(n, current, 0)
    
    return count

def backtrack(n, current, row):
    if row == n:        
        current.pop()
        return current, 1
    count = 0
    for col in range(n):
        if check(current, row, col):
            current.append(col)
            current, c = backtrack(n, current, row + 1)
            count += c
    if len(current) == 0:
        return current, count
    current.pop()
    return current, count

def check(current, row, col):
    for i, c in enumerate(current):
        if c == col or (c + row - i) == col or (c - row + i ) == col:
            return False
    return True
            