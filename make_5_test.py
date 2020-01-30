def solution(N, number):
    ables = [set() for _ in range(9)]
    for i in range(1, 9):
        ables[i].add(int(str(N)*i))
    for i in range(1, 9):        
        # + - / *
        # NNN
        pools = [N]
        # temp = set(ables[i])
        # 5 --> 1 4 / 2 3 , 3 --> 1 2, 2 --> 1 1, 4 --> 1 3 / 2 2
        for x in range(1, (i // 2) + 1):
            y = i - x
            print("zxcv", i, x, y)
            print(ables)
            print(ables[x], ables[y], ables[i])
            for v1 in ables[x]:
                for v2 in ables[y]:
                    ables[i].add(v1 + v2)
                    ables[i].add(v1 - v2)
                    ables[i].add(v2 - v1)
                    ables[i].add(v1 * v2)
                    if not v2 == 0:
                        ables[i].add(v1 // v2)
                    if not v1 == 0:
                        ables[i].add(v2 // v1)
        # for t in temp:
        #     ables[i].add(t)
        if number in ables[i]:
            return i
    return -1
                
if __name__ == '__main__':
    print(solution(5, 12))