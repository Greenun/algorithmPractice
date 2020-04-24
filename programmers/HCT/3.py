def solution(n, m, k):
    MOD = 1000000007
    # kind: 2 (ski, snowboard)
    # each width sum: m // 2
    # 번갈아 배치 = n % 2 == 0: 1가지 / n % 2 == 1: 2가지
    pair = list()
    mul = 1
    if n % 2 == 0:
        pair = [n // 2, n // 2]
    else:
        pair = [n // 2, n // 2 + 1]
        mul = 2
    width = m // 2
    total = cases(width, pair, k)
    total *= mul
    return total

def cases(width, pair, k):
    # (K 이하의)n개의 수로 width를 만드는 경우의 수
    enable = list(range(1, k + 1))
    n, m = pair
    v = n if n > m else m
    dp = [[0]*(width+1) for _ in range(v+1)]
    
    return dp[n][width]*dp[m][width]