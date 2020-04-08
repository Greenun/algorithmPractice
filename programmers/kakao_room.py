# 77.8 - 효율성 실패
def solution(k, room_number):
    from collections import defaultdict
    room_map = defaultdict(list)
    result = list()
    for rn in room_number:
        if room_map.get(rn):
            value = room_map[rn][-1] + 1
            while value <= k:
                if room_map.get(value):
                    room_map[rn].extend(room_map[value])
                    room_map[value] = room_map[rn]
                    value += 1
                else:
                    room_map[value] = room_map[rn]
                    room_map[rn].append(value)
                    result.append(value)
                    break
        else:
            room_map[rn].append(rn)
            result.append(rn)    
    return result

# 77.8 - 효율성만 실패 (최대 단순)
def solution(k, room_number):
    result = list()
    for rn in room_number:
        while rn <= k:
            if rn not in result:
                result.append(rn)
                break
            else:
                rn += 1
    return result

# 통과
def solution(k, room_number):
    from collections import defaultdict
    room_map = defaultdict(list)
    result = list()
    for rn in room_number:
        if room_map.get(rn):
            value = room_map[rn][-1] + 1
            while value <= k:
                if room_map.get(value):
                    # extend 하느라 시간낭비 말고 마지막 부분만 신경쓰면 가능
                    # room_map[rn].extend(room_map[value])
                    room_map[rn].append(room_map[value][-1])
                    room_map[value] = room_map[rn]
                    value = room_map[value][-1] + 1
                else:
                    room_map[value] = room_map[rn]
                    room_map[rn].append(value)
                    result.append(value)
                    break
        else:
            room_map[rn].append(rn)
            result.append(rn)    
    return result

# 다른 풀이 - 위의 list 풀이가 효율성에서는 살짝 빠름
def solution(k, room_number):
    from collections import defaultdict
    room_map = defaultdict(int)
    result = list()
    for rn in room_number:
        temp = list()
        if room_map.get(rn):
            temp.append(rn)
            value = room_map[rn]
            while value <= k:
                if room_map.get(value):
                    temp.append(value)
                    value = room_map[value]
                else:
                    room_map[value] = room_map[temp[-1]] + 1
                    result.append(value)
                    break
            for t in temp:
                room_map[t] = room_map[value]
        else:
            room_map[rn] = rn + 1
            result.append(rn) 
    return result