def solution(N, number):
    S = [{N}]
    # key : N을 몇번 쓰냐가 핵심..
    for i in range(2, 9):
        # print(S)
        lst = [int(str(N)*i)]
        for X_i in range(0, int(i / 2)):
            print(S[X_i], S[i - X_i - 2], i, X_i)
            # N을 몇번 쓰지 구하기 위해 --> e.g., if i == 6 --> 1, 5 / 2, 4 / 3, 3 etc..
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1

if __name__ == '__main__':
    solution(5, 12)
