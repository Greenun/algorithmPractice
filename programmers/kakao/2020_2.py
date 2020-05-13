from itertools import permutations
def solution(expression):
    ops = set()
    max_value = 0
    for c in expression:
        if not c.isdigit():
            ops.add(c)
    generator = permutations(ops)
    for cases in generator:
        result = abs(calculate(expression, cases)[0])
        if max_value < result:
            max_value = result
    return max_value

def tokenize(string):
    operations = list()
    tokens = list()
    temp = ""
    for s in string:
        if s.isdigit():
            temp += s
        else:
            tokens.append(int(temp))
            operations.append(s)
            temp = ""
    if temp:
        tokens.append(int(temp))
    return tokens, operations
        
def calculate(expression, priority):
    tokens, ops = tokenize(expression)
    for pr in priority:
        indices = get_indices(ops, pr)
        for i, idx in enumerate(indices):
            idx -= i
            ops.pop(idx)
            x = tokens.pop(idx)
            y = tokens.pop(idx)
            result = operate(pr, [x, y])
            tokens.insert(idx, result)
    return tokens

def get_indices(ops, target):
    indices = list()
    for i, op in enumerate(ops):
        if op == target:
            indices.append(i)
    return indices
    
def operate(exp, numbers):
    x, y = numbers
    if exp == "*":
        return x * y
    elif exp == "-":
        return x - y
    else:
        return x + y