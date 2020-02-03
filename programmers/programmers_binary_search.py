def solution(budgets, M):
    answer = 0
    budgets.sort()
    num = len(budgets)
    # condition: (M - sum(:idx+1)) // remains > budgets[idx+1] else stop
    start = 0
    end = num - 1
    while start < end:        
        idx = (start + end) // 2
        med = budgets[idx]
        remains = num - (idx + 1)
        if ((M - sum(budgets[:idx+1])) // remains) > budgets[idx + 1]:
            if not idx + 2 >= num:
                if not ((M - sum(budgets[:idx+2])) // remains) > budgets[idx + 2]:
                    start = idx + 1
                    break
                else:
                    start = idx + 1
            else:
                start = idx + 1
        else:
            end = idx
    if start == num - 1:
        return budgets[start]
    elif start == 0:
        if (M // num) < budgets[start]:
            return (M // num)
    target = budgets[start]
    total = target * (num - (start+1)) + sum(budgets[:start+1])
    upper_limit = target + ((M - total) // (num - (start+1)))
    return upper_limit
