def solution(inputString):
    stacks = [list() for _ in range(4)]
    count = 0
    for s in inputString:
        if s == "(" or s == ")":
            stacks[0].append(s)
        elif s == "{" or s == "}":
            stacks[1].append(s)
        elif s == "[" or s == "]":
            stacks[2].append(s)
        elif s == "<" or s == ">":
            stacks[3].append(s)
    for stack in stacks:
        close_b = list()
        while stack:
            v = stack.pop()
            if v == ")" or v == "}" or v == "]" or v == ">":
                close_b.append(v)
            else:
                if close_b:
                    close_b.pop()
                    count += 1
                else:
                    return -1
        if close_b:
            return -1
    return count