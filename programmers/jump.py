def solution(n):
    # 1
    # 1 1 / 2 -> 2
    # 1 1 1 / 1 2 / 2 1 -> 3
    # 1 1 1 1 / 1 1 2 (3)/ 2 2 -> 5
    # 1 1 1 1 1 / 1 1 1 2 (4)/ 1 2 2 (3) -> 8
    # 5 --> 5C0 + 4C1 + 3C2
    # r == 0 : 1
    # r == 1 : n - r C r
    # n C r --> n! // (n-r)!r!
    _sum = 0
    for r in range(n // 2 + 1):
        _sum += factorial(n - r) // (factorial(n - 2*r)*factorial(r))
    return _sum % 1234567

def factorial(n):
    mul = 1
    for i in range(1, n + 1):
        mul *= i
    return mul

# 다른 풀이(피보나치) - 훨씬 빠름 - 다만 근거가 부족한 것처럼 보임
def solution(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567
