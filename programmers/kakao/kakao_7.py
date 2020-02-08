def solution(board):
    from collections import defaultdict
    n = len(board)
    actions = defaultdict(set)
    actions[0].add(((1,1), (1,2)))
    total = {((1, 1), (1, 2))}
    tries = 1
    while 1:
        for action in actions[tries-1]:
            for able in ables(action, board):
                if not all(x >= 1 and x <= n for x in [
                    able[0][0], able[0][1], able[1][0], able[1][1]
                ]):
                    continue
                elif (board[able[0][0]-1][able[0][1]-1] == 1 or
                	board[able[1][0]-1][able[1][1]-1] == 1):
                	continue
                else:
                    if able in total:
                        continue
                    else:    
                        actions[tries].add(able)
                        total.add(able)
        if {((n - 1, n), (n, n)), ((n, n - 1), (n, n))} & actions[tries]:
            return tries
        tries += 1


def ables(action, board):
    one = action[0]
    two = action[1]
    hor = (one[0] == two[0])
    ret = [
        ((one[0]+1, one[1]), (two[0]+1, two[1])), # under
        ((one[0]-1, one[1]), (two[0]-1, two[1])), # up
        ((one[0], one[1]+1), (two[0], two[1]+1)), # right
        ((one[0], one[1]-1), (two[0], two[1]-1)) # left
    ]
    if hor:
        if all(x < len(board) for x in [one[0], two[0]])\
        and board[one[0]][one[1]-1] == 0 and board[two[0]][two[1]-1] == 0:
            ret.extend([
                (two, (one[0]+1, one[1]+1)),
                (one, (two[0]+1, two[1]-1))
            ])
        if all(x > 1 for x in [one[0], two[0]]) \
        and board[one[0]-2][one[1]-1] == 0 and board[two[0]-2][two[1]-1] == 0:
            ret.extend([            
                ((one[0]-1, one[1]+1), two),
                ((two[0]-1, two[1]-1), one),
            ])
        return ret
    else:
        if all(x < len(board) for x in [one[1], two[1]]) and\
        board[one[0]-1][one[1]] == 0 and board[two[0]-1][two[1]] == 0:
            ret.extend([
                (one, (two[0]-1, two[1]+1)),    
                (two, (one[0]+1, one[1]+1))
            ])
        if all(x > 1 for x in [one[1], two[1]]) and\
        board[one[0]-1][one[1]-2] == 0 and board[two[0]-1][two[1]-2] == 0:
            ret.extend([
                ((one[0]+1, one[1]-1), two),
                ((two[0]-1, two[1]-1), one)
            ])
        return ret