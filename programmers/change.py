# 효율성 시간초과
def solution(n, money):
    dp = [[1]+ [0]*(n) for _ in range(len(money))]
    # 1 / 1 1, 2 / 1 1 1, 1 2 / 1 1 1 1, 1 1 2, 2 2 / 1 1 1 1 1, 1 1 1 2, 1 2 2, 5
    # 1 1 1 1 1 1, 1 1 1 1 2, 1 1 2 2, 2 2 2, 1 5
    # 1 1 1 1 1 1 1, 1 1 1 1 1 2, 1 1 1 2 2, 1 2 2 2, 1 1 5, 2 5
    # [2, 3, 5, 6]
    # 2 / 3 / 2 2 / 2 3, 5 / 2 2 2, 3 3, 6 / 2 2 3, 2 5 / 2 2 2 2, 2 3 3, 3 5, 2 6 (8)
    m = money.pop(0)
    for i in range(1, n + 1):
        if i % m == 0:
            dp[0][i] = 1
    for i, m in enumerate(money):
        for j in range(1, n+1):
            temp = j
            while temp >= 0:
                dp[i+1][j] += (dp[i][temp]) % 1000000007
                temp -= m
    return dp[-1][n]
            
# 효율성 2개 통과
def solution(n, money):
    dp = [1] + ([0] * (n))
    for m in money:
        for j in range(n, 0, -1):
            temp = j - m
            while temp >= 0:
                dp[j] += dp[temp]
                temp -= m
    return dp[n] % 1000000007
                
# 효율성 통과
def solution(n, money):
    dp = [1] + ([0] * (n))
    m = money.pop(0)
    for i in range(0, n + 1, m):
        dp[i] = 1
    for m in money:
        for j in range(n, m-1, -1):
            temp = j - m
            while temp >= 0:
                dp[j] += dp[temp]
                temp -= m
    return dp[n] % 1000000007

# 더 효율적 (다른 사람 답 참고)
def solution(n, money):
    dp = [1] + ([0] * (n))
    m = money.pop(0)
    for i in range(0, n + 1, m):
        dp[i] = 1
    for m in money:
        for j in range(m, n + 1):
            dp[j] += dp[j - m]
    return dp[n] % 1000000007
