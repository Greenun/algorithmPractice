# 효율성 실패
def solution(n, k):
    from itertools import permutations
    line = list(range(1, n + 1))
    gen = permutations(line, n)
    for i, v in enumerate(gen):
        if i + 1 == k:
            return list(v)

# k // (n - 1)!
# k = 4 -> 2 3 1 ==> 4 // 2 --> 2 ==> 2 // 1 --> 2
# k = 5 -> 3 1 2 ==> 5 // 2 --> 2.5 --> 3 ==> 

def solution(n, k):
    import math
    factorials = factorial(n)
    numbers = list(range(1, n + 1))
    current = k
    answer = list()
    for temp in range(n, 0, -1):
        # print(temp, current, answer, factorials[temp - 2])
        min_idx = math.ceil(current / factorials[temp - 2])
        value = numbers.pop(min_idx - 1)
        answer.append(value)
        current -= (min_idx-1)*factorials[temp - 2] # 이 부분은 나머지 연산으로 고칠 수 있을 듯
        # current = current % factorials[temp - 2]
    return answer
    
def factorial(x):
    l = list([1])
    for i, v in enumerate(range(2, x + 1)):
        l.append(l[i]*v)
    return l
