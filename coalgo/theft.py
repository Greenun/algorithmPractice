def solution(money):
    n = len(money)
    # 2 cases
    # must go first hose
    dp = [0]*n
    dp[0] = money[0]
    dp[1] = (max(dp[0], money[1]))
    for i in range(2, n-1): 
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    # must go last house
    adp = [0]*n
    adp[0] = 0
    adp[1] = money[1]
    for i in range(2, n):
        adp[i] = max(adp[i-2] + money[i], adp[i-1])
    return max(max(dp), max(adp))
