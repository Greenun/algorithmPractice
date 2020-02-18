def check_match(lock, key):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] + key[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True
    m = len(key[0])
    n = len(lock[0])

    new_key_0 = [[0] * n for _ in range(n)]
    new_key_1 = [[0] * n for _ in range(n)]
    new_key_2 = [[0] * n for _ in range(n)]
    new_key_3 = [[0] * n for _ in range(n)]
    # rotate 부분!
    for i in range(m):
        for j in range(m):
            new_key_0[i][j] = key[i][j]
            new_key_1[j][m-i-1] = key[i][j]
            new_key_2[m-i-1][m-j-1] = key[i][j]
            new_key_3[m-j-1][i] = key[i][j]
    # 와...
    for key in [new_key_0, new_key_1, new_key_2, new_key_3]:
        for i in range(n):
            for j in range(n):
                left_up_key = [row[i:] + [0]*i for row in key[j:]] + [[0]*n]*j
                if check_match(lock, left_up_key):
                    return True
                left_down_key = [[0]*n]*(n-j-1) + [row[i:] + [0]*i for row in key[:j+1]]
                if check_match(lock, left_down_key):
                    return True
                right_up_key = [[0]*i + row[:n-i] for row in key[j:]] + [[0]*n]*j
                if check_match(lock, right_up_key):
                    return True
                right_down_key = [[0]*n]*(n-j-1) + [[0]*i + row[:n-i] for row in key[:j+1]]
                if check_match(lock, right_down_key):
                    return True
    return False

# 와 좌표로.. 90도 변환 시 M - 1 - y좌표, x 좌표.. 신기..
# 구멍 좌표를 구한 후 이동시키면서 좌표가 일치하는지 확인.. --> 매 시도마다 90도 왼쪽 회전..
def solution(key, lock):
    hole = set()
    N = len(lock)
    M = len(key)
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                hole.add((i,j))

    key_hole = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_hole.append((i,j))

    if len(hole) > len(key_hole):
        return False

    for _ in range(4):
        for y in range(-N + 1, M + N):
            for x in range(-N + 1, M + N):
                answer = set(hole)
                is_valid = True
                for k in key_hole:
                    k_y = k[0] + y
                    k_x = k[1] + x
                    if (k_y, k_x) in answer:
                        answer.remove((k_y, k_x))
                    elif k_y < 0 or k_y >= N or k_x < 0 or k_x >= N:
                        continue
                    else:
                        is_valid = False
                        break

                if len(answer) == 0 and is_valid:
                    return True

        for i in range(len(key_hole)):
            p = key_hole[i]
            key_hole[i] = (M - p[1] - 1, p[0])

    return False

# 내 풀이 였던 것
def solution(key, lock):
    answer = False
    rot90 = rotate(key)
    rot180 = rotate(rot90)
    rot270 = rotate(rot180)
    x1 = match(key, lock)
    x2 = match(rot90, lock)
    x3 = match(rot180, lock)
    x4 = match(rot270, lock)
    answer = x1 or x2 or x3 or x4
    # print("key: ",key)
    # print("rot90: ", rot90)
    # print("rot180: ", rot180)
    # print("rot270: ", rot270)
    
    return answer

# def get_four_points(matrix):
#     t = 0
#     for i in range(len(matrix)):
#         for j in matrix[i]:
#             if j == t:
#                 top = (i, matrix[i].index(j))
#     for i in range(len(matrix)-1, -1, -1):
#         for j in matrix[i]:
#             if j == t:
#                 bottom = (i, matrix[i].index(j))
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[j][i] == t:
#                 left = (i, j)
#     for i in range(len(matrix)-1, -1, -1):
#         for j in range(len(matrix)-1, -1, -1):
#             if matrix[j][i] == t:
#                 right = (i, j)
#     return top, bottom, left, right

def match(key, lock):
    n = len(lock)
    import copy
    extended_lock = []
    for i in range(3*n):
        temp = copy.deepcopy([0]*(3*n))
        extended_lock.append(temp)
    # init
    for i, row in enumerate(lock):
        for j in range(n):
            extended_lock[n+i][n+j] += row[j]
    m = len(key)
    result = False
    for i in range(n-m+1, 2*n):
        for j in range(n-m+1, 2*n):
            result = add_check(copy.deepcopy(extended_lock), key, n, m, i, j)
            # print("i,j,result: ",i, j, result)
            if result: return True
    return result
    
            
def add_check(ext_lock, key, n, m, s1, s2):
    for i in range(0, m):
        for j in range(0, m):
            ext_lock[s1+i][s2+j] += key[i][j]
    # n,n ~ 2n-1, 2n-1
    is_match = False
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            # print(i, j)
            if not ext_lock[i][j] == 1:
                # is_match = False
                # break
                # print("lock: ", ext_lock)
                return False
            else:
                is_match = True
    # print(is_match, ext_lock)
    # print("true???: ", is_match)
    return is_match
                
            
    
def rotate(key):
    # rot90 left
    import copy
    temp = copy.deepcopy(key)
    for idx, k in enumerate(key):
        for i in range(len(k)):
            t = copy.deepcopy(k)
            t.reverse()
            temp[i][idx] = t[i]
    return temp