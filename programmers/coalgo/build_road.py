def solution(board):
    # BFS + direction information ( for calc cost )
    n = len(board)
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    from collections import deque
    queue = deque()
    cost_map = dict()
    queue.append((0, 0, -1, 0))
    min_value = float('inf')
    while queue:
        current = queue.popleft()
        x, y, direction, c = current
        for i in range(4):
            dx, dy = directions[i]
            nx = x + dx
            ny = y + dy
            cost = c
            #
            if not ((0 <= nx < n) and (0 <= ny < n)) or board[nx][ny] == 1:
                continue
            if direction == -1:
                # init
                cost += 100
            elif (direction - i) % 2 == 0:
                # same direction
                cost += 100
            else:
                # other direction
                cost += 600
            if (nx, ny) == (n - 1, n - 1):
                min_value = cost if cost < min_value else min_value
            elif cost_map.get((nx, ny, i)) is None or cost_map.get((nx, ny, i)) > cost:
                cost_map[(nx, ny, i)] = cost
                queue.append((nx, ny, i, cost))
    return min_value

