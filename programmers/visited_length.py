def solution(dirs):
    visited = set()
    current = (0, 0)
    bl, bm = (-5, 6)
    for op in dirs:
        x, y = current
        if op == 'L':
            if not x - 1 in range(bl, bm):
                continue
            visited = visited.union({(current, (x - 1, y)), ((x - 1, y), current)})
            current = (x - 1, y)
        elif op == 'R':
            if not x + 1 in range(bl, bm):
                continue
            visited = visited.union({(current, (x + 1, y)), ((x + 1, y), current)})
            current = (x + 1, y)
        elif op == 'U':
            if not y + 1 in range(bl, bm):
                continue
            visited = visited.union({(current, (x, y + 1)), ((x, y + 1), current)})
            current = (x, y + 1)
        else:
            if not y - 1 in range(bl, bm):
                continue
            visited = visited.union({(current, (x, y - 1)), ((x, y - 1), current)})
            current = (x, y - 1)
    return len(visited) // 2