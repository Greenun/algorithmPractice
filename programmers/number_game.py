# 효율성 2개 실패
def solution(A, B):
    B.sort()
    A.sort()
    score = 0
    ai, bi = 0, 0
    while len(A) > 0:
        if A[ai] < B[bi]:
            score += 1
            A.pop(ai)
            B.pop(bi)
            ai, bi = 0, 0
        else:
            bi += 1
            if bi >= len(B):
                break
    return score

# binary search 도입 아슬하게 성공..
def solution(A, B):
    B.sort()
    A.sort()
    score = 0
    while len(A) > 0:
        a = A.pop(0)
        idx = search(a, B)
        while idx < len(B) - 1:
            if B[idx] > a:
                break
            idx += 1
        if B[idx] > a:
            score += 1
        B.pop(idx)
    return score

def search(a, B):
    low = 0
    high = len(B) - 1
    while low < high:
        mid = (low + high) // 2
        if B[mid] > a:
            high = mid
        elif B[mid] < a:
            low = mid + 1
        else:
            break
    return low
    
# 다른 풀이 -> 간단, 빠름
def solution(A, B):
    B.sort()
    A.sort()
    score = 0
    for _ in range(len(A)):
        if A[-1] < B[-1]:
            score += 1
            A.pop()
            B.pop()
        else:
            A.pop()
            B.pop(0)
    return score