def solution(board, moves):
    stacks = [list() for _ in range(len(board[0]))]
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[i])):
            if not board[i][j] == 0:
                stacks[j].append(board[i][j])
    basket = list()
    print(stacks)
    pang = 0
    for move in moves:
        if not stacks[move - 1]:
            continue
        value = stacks[move - 1].pop()
        if basket:
            if basket[-1] == value:
                basket.pop()
                pang += 2
                continue
        basket.append(value)
    return pang