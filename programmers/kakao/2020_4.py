def solution(board):
    from collections import defaultdict
    n = len(board)
    visited = set()
    stack = [(0, 0)]
    route = list()
    routes = list()
    depth = 0
    depth_map = defaultdict(list)
    while stack:
        current = stack.pop()
        route.append(current)
        cx, cy = current
        moves = check(n, board, cx, cy, visited)
        if not moves:
            depth -= 1
        else:
            depth += 1
            depth_map[depth].extend(moves)
            stack.extend(moves)
        visited.add(current)
        if len(route) == len(visited):
            routes.append(route)
        print(depth_map)
    
def check(n, board, cx, cy, visited):
    result = list()
    moves = [(cx + 1, cy), (cx, cy + 1), (cx - 1, cy), (cx, cy - 1)]
    for move in moves:
        x, y = move
        if move in visited or x >= n or y >= n or x < 0 or y < 0:
            continue
        else:
            if board[x][y] == 1:
                continue
            result.append(move)
    return result
        
# def backtrack(n, board, visited, routes):
#     if routes[-1] == [n-1, n-1]:
#         global all_cases
#         all_cases.append(routes)
#         return
#     current = routes[-1]
#     cx, cy = current
#     moves = [(cx + 1, cy), (cx, cy + 1), (cx - 1, cy), (cx, cy - 1)]
#     for move in moves:
#         x, y = move
#         if move in visited or x >= n or y >= n or board[x][y] == 1:
#             continue
#         visited.add(move)
#         temp_routes = routes[:]
#         temp_routes.append(move)
#         backtrack(n, board, visited, temp_routes)