def solution(n, s):
    if n > s:
        return [-1]
    remainder = s % n
    quotient = s // n
    number_set = [quotient for _ in range(n)]
    idx = len(number_set) - 1
    for i in range(remainder):
        number_set[idx - i] += 1
    return number_set
