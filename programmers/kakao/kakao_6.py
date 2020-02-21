from itertools import permutations, combinations

# 내 풀이 (작성이 오래걸림)
def solution(n, weak, dist):
    from itertools import permutations
    dist = [d + 1 for d in dist]
    dist.sort(reverse=True)
    mins = 10
    for dist_perm in permutations(dist):
        res = travel(dist_perm, weak, n)
        mins = res if mins > res else mins
    if mins < 9:
        return mins
    else:
        return -1

def travel(dist_perm, weak, n):
    minimum = 10
    for pattern in generate_pattern(weak):
        result = 0
        i = 0
        for idx, d in enumerate(dist_perm):
            if i >= len(pattern): break
            g = pattern[i]
            bits = build_bits(n, d, g)
            result |= bits
            while result & (1 << g) != 0:
                i += 1
                if i >= len(pattern):
                    minimum = idx + 1 if minimum > idx + 1 else minimum
                    break
                g = pattern[i]
    return minimum

def build_bits(n, d, w):
    if w + d > n - 1:
        return (((2**(n-w) - 1) << w) | (2**(w+d-n) - 1))    
    else:
        return (2**d - 1) << w

def generate_pattern(origin):
    for i in range(len(origin)):
        yield origin[i:] + origin[:i]

from collections import deque

def solution2(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    # q = [weak[:]]
    visited = set()
    visited.add(tuple(weak))
    print(q, visited, dist)
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                print(f"l, r: {l}, {r}")
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))
                x = tuple([m for m in current if m not in temp])
                if len(temp) == 0:
                    return (i + 1)
                # elif temp not in visited:
                elif x not in visited:
                    # visited.add(temp)
                    visited.add(tuple(x))
                    q.append(list(temp))
            #     print("d: ", d, "q: ", q, "visited: ", visited)
            # print("current loop result -> visited: ", visited, "q: ", q)
    return -1

# list로 할 경우 시간초과
def solution(n, weak, dist):
    dist.sort(reverse=True)
    # queue = list()
    # queue.append(weak[:])
    queue = set()
    queue.add(tuple(weak[:]))
    visited = set()
    for i, d in enumerate(dist):
        if d >= n: return 1
        copies = set(queue)
        for _ in range(len(queue)):
            # current = queue.pop(0)
            current = copies.pop()
            for c in current:                
                st, ed = c, (c + d) % n
                temp = current[:]
                visited.add((st, ed))
                if st < ed:
                    temp = [t for t in temp if t < st or t > ed]
                else:
                    temp = [t for t in temp if t > ed and t < st]
                if not temp:
                    return i + 1
                # if temp not in queue:
                #     queue.append(temp)
                queue.add(tuple(temp))
    return -1

if __name__ == '__main__':
    print(solution2(12, [1, 5, 6, 10], [1,2,3,4]))
    print(solution2(12, [1, 3, 4, 9, 10], [3, 5, 7]))