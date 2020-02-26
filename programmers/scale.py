# 다음 원소와의 차이가 0 이하: next sum - range(sum) 으로 cover
# 다음 원소와의 차이가 1: 다음 원소가 sum + 1 -> cover
def solution(weight):
    weight.sort()
    current_sum = 0
    for i in range(len(weight) - 1):
        current_sum += weight[i]
        next_value = weight[i+1]
        if current_sum + 1 >= next_value:
            continue
        else:
            return current_sum + 1
    return current_sum + weight[len(weight)-1] + 1