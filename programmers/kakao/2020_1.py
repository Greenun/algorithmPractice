def solution(numbers, hand):
    answer = ""
    left_pool = [1,4,7]
    right_pool = [3,6,9]
    hand = True if hand == "right" else False
    current_left, current_right = [3, 0], [3, 2]
    for number in numbers:
        choice = ""
        target = get_point(number)
        if number in left_pool:
            choice = "L"
        elif number in right_pool:
            choice = "R"
        else:
            left_dist = get_distance(target, current_left)
            right_dist = get_distance(target, current_right)
            if left_dist == right_dist:
                if hand:
                    choice = "R"
                else:
                    choice = "L"
            elif left_dist > right_dist:
                choice = "R"
            else:
                choice = "L"
        answer += choice
            
        if choice == "R":
            current_right = target
        else:
            current_left = target
        
    return answer

def get_point(number):
    if number == 0:
        number = 11
    return [(number - 1) // 3, (number - 1) % 3]
            
def get_distance(target, current):
    tx, ty = target
    cx, cy = current
    return abs(tx - cx) + abs(ty - cy)