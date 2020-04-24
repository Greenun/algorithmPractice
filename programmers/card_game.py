def solution(left, right):
    dp = [[0]*(len(right)+1) for _ in range(len(left)+1)]
    # 큰 수부터 하면 안되는
    for i in range(len(left)-1, -1, -1):
        for j in range(len(right)-1, -1, -1):
            if left[i] > right[j]:
                dp[i][j] = dp[i][j+1] + right[j]
            else:
                dp[i][j] = max(dp[i+1][j+1], dp[i+1][j])
    return dp[0][0]