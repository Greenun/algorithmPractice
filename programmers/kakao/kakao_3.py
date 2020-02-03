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