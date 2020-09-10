def solution(expression):
    from itertools import permutations
    result = list()
    numbers = list()
    exps = list()
    word = ""
    for c in expression:
        if c.isdigit():
            word += c
        else:
            numbers.append(int(word))
            word = ""
            exps.append(c)
    numbers.append(int(word)) # last number
    
    for order in permutations(['*', '-', '+'], 3):
        result.append(abs(calculate(order, numbers[:], exps[:])))
    
    return max(result)

def calculate(order, numbers, exps):
    temp = list()
    temp_numbers = numbers[:]
    for o in order:
        idx = 0
        for _ in range(len(exps)):
            exp = exps.pop(0)
            if exp == o:
                x = numbers.pop(idx)
                y = numbers.pop(idx)
                result = operate(x, y, exp)
                numbers.insert(idx, result)
            else:
                temp.append(exp)
                idx += 1
        exps = temp[:]
        temp = list()
    return numbers[0]

def operate(x, y, exp):
    if exp == "*":
        return x * y
    elif exp == "+":
        return x + y
    else:
        return x - y
