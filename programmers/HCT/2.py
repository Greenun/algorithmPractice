def solution(id_list, k):
    from collections import defaultdict
    coupons = defaultdict(int)
    for user_str in id_list:
        user_list = user_str.split(' ')
        for user in set(user_list):
            if coupons[user] < k:
                coupons[user] += 1
    _sum = 0
    for k in coupons:
        _sum += coupons[k]
    return _sum