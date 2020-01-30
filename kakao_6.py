from itertools import permutations, combinations

def solution(n, weak, dist):
    answer = 0 
    dist = [d + 1 for d in dist]
    for i in range(1, len(dist)+1):        
        for p in permutations(dist, i):
            if travel(p, weak, n):
                return i
    
    return -1

def travel(dist_perm, weak, n):
    l = len(dist_perm)
    for pattern in generate_weaks(n, weak):
        result = 0
        i = 0
        for d in dist_perm:
            if i >= len(pattern): break
            g = pattern[i]
            bits = build_bits(n, d, g)
            result |= bits
            while result & (1 << g) != 0:
                i += 1
                if i >= len(pattern):
                    return True
                g = pattern[i]
    return False
#     for points in combinations(weak, l):
#         for j in range(2**l):
#             temp = []
#             result = 0
#             swap_bits = '{0:b}'.format(j).zfill(l)
#             for idx, d in enumerate(dist_perm):
#                 temp.append(build_bits(n, d, points[idx], swap_bits[idx]))
                
#             for t in temp:
#                 result |= t
#             # if dist_perm == (3,6,8) or dist_perm == (4,6,8):
#             #     print("points, temp: ", points, temp)
#             #     print(f"{dist_perm}", "{0:b}".format(result).zfill(n))    
#             # if temp == [28, 33030144, 130560]:
#             #     print('result: ','{0:b}'.format(result).zfill(n))
#             #     print('goal:', '{0:b}'.format(goal).zfill(n))
#             if check_goal(result, goal):
#                 return True
    # return False

def build_bits(n, d, w, swap='0'):
    if w + d > n - 1:
        # e.g., 110000 (2, 5) --> 100001 2, 5, 6
        # n - w # left
        # w + d - n # right
        return (((2**(n-w) - 1) << w) | (2**(w+d-n) - 1))    
    else:
        return (2**d - 1) << w
#     if swap == '0':
#         # left
#         if w + d > n - 1:
#             # e.g., 110000 (2, 5) --> 100001 2, 5, 6
#             # n - w # left
#             # w + d - n # right
#             return (((2**(n-w) - 1) << w) | (2**(w+d-n) - 1))
            
#         else:
#             return (2**d - 1) << w
#     else:
#         # right
#         if w - d < 0:
#             # e.g., 000011 (2, 1) --> 100001
#             # d - w - 1 # left
#             # w + 1 # right
#             return ((2**(d-w-1) - 1) << n - d + w | (2**(w+1) - 1))
#         else:
#             return (2**d - 1) << w - d + 1

def generate_weaks(n, weak):
    for i in range(len(weak)):
        yield weak[i:] + weak[:i]
        
# def check_goal(target, goal):
#     return (target & goal) == goal

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
            # current = q.pop(0)
            for p in current:
                l = p
                r = (p + d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))

                if len(temp) == 0:
                    return (i + 1)
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
                print("d: ", d, "q: ", q, "visited: ", visited)
            print("visited: ", visited, "q: ", q)
    return -1

if __name__ == '__main__':
    solution2(12, [1, 5, 6, 10], [1,2,3,4])
    solution2(12, [1, 3, 4, 9, 10], [3, 5, 7])