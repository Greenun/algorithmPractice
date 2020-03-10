def solution(n):
    result = list()
    result = move(1, 2, 3, n - 1, result)
    result = move(1, 3, 2, 1, result)
    result = move(2, 3, 1, n - 1, result)
    return result

def move(_from, _to, _by, n, result):
    # (1, 3, 2, 1) --> [1, 3]
    # (1, 2, 3, 2)
    # (1, 3, 2, 2) --> [1, 2] [1, 3] [2, 3]
    # (1, 3, 2, 3) --> [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]
    if n == 1:
        result.append([_from, _to])
        return result
    result = move(_from, _by, _to, n - 1, result)
    result = move(_from, _to, _by, 1, result)
    result = move(_by, _to, _from, n - 1, result)
    return result

# iterative version
def solution(n):
    _from, _by, _to = list(), list(), list()
    f, b, t = [1, 2, 3] if n % 2 == 1 else [1, 3, 2]
    for i in range(n, 0, -1):
        _from.append(i)
    result = list()
    forward = True
    for i in range(1, 2**n):
        movement = None
        if i % 3 == 0:
            forward = move(_by, _to)
            movement = [b, t] if forward else [t, b]
        elif i % 3 == 1:
            forward = move(_from, _to)
            movement = [f, t] if forward else [t, f]
        else:
            forward = move(_from, _by)
            movement = [f, b] if forward else [b, f]
        result.append(movement)
    return result
        
def move(pole_one, pole_two):
    if len(pole_one) == 0:
        pole_one.append(pole_two.pop())
        return False
    elif len(pole_two) == 0:
        pole_two.append(pole_one.pop())
        return True
    else:
        one = pole_one.pop()
        two = pole_two.pop()
        if one > two:
            pole_one += [one, two]
            return False
        else:
            pole_two += [two, one]
            return True