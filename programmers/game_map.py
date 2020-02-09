# 효율성 실패 (DFS)
# def solution(maps):
#     from collections import defaultdict
#     n = len(maps) # rows
#     m = len(maps[0]) # cols
#     actions = defaultdict(set)
#     actions[0].add((1, 1))
#     move = 1
#     total = [(1, 1)]
#     while move < m*n:
#         for action in actions[move-1]:
#             for able in ables(maps, action):
#                 if able in total:
#                     continue
#                 else:
#                     total.append(able)
#                     actions[move].add(able)
#         if (n, m) in actions[move]:
#             return move + 1
#         move += 1
#     return -1

# def ables(maps, point):
#     x = point[0]
#     y = point[1]
#     ret = list()
#     if x < len(maps) and maps[x][y-1] == 1:
#         ret.append((x + 1, y))
#     if x > 1 and maps[x-2][y-1] == 1:
#         ret.append((x - 1, y))
#     if y < len(maps[0]) and maps[x-1][y] == 1:
#         ret.append((x, y + 1))
#     if y > 1 and maps[x-1][y-2] == 1:
#         ret.append((x, y - 1))
#     return ret

# BFS로 해결

def solution(maps):
    from collections import defaultdict
    n = len(maps) # rows
    m = len(maps[0]) # cols
    move = 1
    queue = [(1, 1)]
    visited = set()
    children = 1
    while queue:
        for i in range(children):
            point = queue.pop(0)
            if not point in visited:
                enable = ables(maps, point)
                queue.extend(enable)
                visited.add(point)
        children = len(queue)
        if (n, m) in visited:
            return move
        move += 1
    return -1

def ables(maps, point):
    x, y = point
    ret = list()
    if x < len(maps) and maps[x][y-1] == 1:
        ret.append((x + 1, y))
    if y < len(maps[0]) and maps[x-1][y] == 1:
        ret.append((x, y + 1))
    if x > 1 and maps[x-2][y-1] == 1:
        ret.append((x - 1, y))
    if y > 1 and maps[x-1][y-2] == 1:
        ret.append((x, y - 1))
    return ret