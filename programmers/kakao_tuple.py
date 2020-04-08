import heapq
def solution(s):
    queue = string_to_queue(s)
    answer = list()
    compare_set = set()
    while queue:
        _, value = heapq.heappop(queue)
        element = (value - compare_set).pop()
        answer.append(element)
        compare_set = value
    return answer

def string_to_queue(s):
    s = s[1:-1]
    result = list()
    temp = set()
    integer = ""
    for c in s:
        if c == "{":
            temp = set()
        elif c == "}":
            temp.add(int(integer))
            heapq.heappush(result, (len(temp), temp))
            integer = ""
        elif c == ",":
            if integer:
                temp.add(int(integer))
                integer = ""
        else:
            integer += c
    return result