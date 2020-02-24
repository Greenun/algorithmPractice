def solution(n):
    dp = [0]*(n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = ((dp[i-2] * 2) + dp[i-3]) % 1000000007 # 왜 빨라질까..
    return dp[n] % 1000000007


# 너무 길긴 길다..
def solution(board):
    from collections import defaultdict
    n = len(board)
    moves = defaultdict(set)
    total = set()
    moves[0].add(((1,1), (1,2)))
    total.add(((1,1), (1,2)))
    visited = set()
    count = 1
    while 1:
        for move in moves[count - 1]:
            for enable in check(board, move):
                if enable in total:
                    continue
                moves[count].add(enable)
                total.add(enable)
        if ((n - 1, n), (n, n)) in moves[count] or ((n, n - 1), (n, n)) in moves[count]:
            return count
        count += 1
    
def check(board, current):
    n = len(board)
    first, second = current
    fx, fy = first
    sx, sy = second
    enable = list()
    # ver
    if not fx == sx:
        # up, down
        if fx >= 2 and board[fx - 2][fy - 1] == 0:
            enable.append(((fx - 1, fy), first))
        if sx < n and board[sx][sy - 1] == 0:
            enable.append((second, (sx + 1, sy)))

        # rotate left right
        if fy >= 2 and sy >= 2 and board[fx - 1][fy - 2] == 0 and board[sx - 1][sy - 2] == 0:
            enable.append(((fx, fy - 1), (sx, sy - 1)))
            enable.append(((sx - 1, sy - 1), first))
            enable.append(((fx + 1, fy - 1), second))
        if fy < n and sy < n and board[fx - 1][fy] == 0 and board[sx - 1][sy] == 0:
            enable.append(((fx, fy + 1), (sx, sy + 1)))
            enable.append((first, (sx - 1, sy + 1)))
            enable.append((second, (fx + 1, fy + 1)))
    else:        
        # hor
        # left, right
        if sy < n and board[sx - 1][sy] == 0:
            enable.append((second, (sx, sy + 1)))
        if fy >= 2 and board[fx - 1][fy - 2] == 0:
            enable.append(((fx, fy - 1), first))
        
        # rotate up down
        if fx < n and sx < n and board[fx][fy - 1] == 0 and board[sx][sy - 1] == 0:
            enable.append(((fx + 1, fy), (sx + 1, sy)))
            enable.append((second, (fx + 1, fy + 1)))
            enable.append((first, (sx + 1, sy - 1)))
        if fx >= 2 and sx >= 2 and board[fx - 2][fy - 1] == 0 and board[sx - 2][sy - 1] == 0:
            enable.append(((fx - 1, fy), (sx - 1, sy)))
            enable.append(((sx - 1, sy - 1), first))
            enable.append(((fx - 1, fy + 1), second))
    return enable