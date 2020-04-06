def solution(answer_sheet, sheets):
    from itertools import combinations
    result = list()
    for sheet in sheets:
        temp = list()
        for i in range(len(answer_sheet)):
            if answer_sheet[i] != sheet[i]:
                temp.append((i, sheet[i]))
        result.append(temp)
    max_doubt = 0
    for cases in combinations([x for x in range(len(result)) if len(result[x]) != 0], 2):
        temp = list()
        first, second = cases
        r1, r2 = result[first], result[second]
        for i1, e1 in r1:
            for i2, e2 in r2:
                if i1 == i2 and e1 == e2:
                    temp.append((i1, e1))
        prev = -3
        cont = 1
        ct = 1
        for i in range(len(temp)):
            idx, _ = temp[i]
            if idx == prev + 1:
                ct += 1
            else:
                cont = ct
                ct = 1
            prev = idx
        doubt = len(temp) + cont**2 if len(temp) > 0 else 0
        if max_doubt < doubt:
            max_doubt = doubt
    return max_doubt