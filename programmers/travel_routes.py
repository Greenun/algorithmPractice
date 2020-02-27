# 실패
def solution(tickets):
    from collections import defaultdict
    routes = list()
    airlines = defaultdict(list)
    for departure, arrival in tickets:
        airlines[departure].append(arrival)
    stack = list()
    stack.append("ICN")
    visited = list()
    while stack:
        print(stack, visited)
        current = stack.pop()
        if current in visited:
            visited.append(current)
            continue
        for airport in sorted(airlines[current], reverse=True):
            stack.append(airport)
        visited.append(current)
    return visited
    

def solution(tickets):
    from collections import defaultdict
    airlines = defaultdict(list)
    for departure, arrival in tickets:
        airlines[departure].append(arrival)
    for a in airlines:
        airlines[a].sort()
    current = "ICN"
    visited = list()
    while len(visited) < len(tickets):
        # print(visited)
        if not airlines[current]:
            # 성공하지 못하고 갈 경로가 없는 경우
            # 갈 경로가 2개 이상인 위치까지 롤백(1개인 경우는 다른 경우의 수가 없으므로)
            # 롤백 시 후순위로 append
            while len(airlines[current]) < 2:
                st, ed = visited.pop()
                airlines[st].append(ed)
                current = st
        else:
            # 일반적인 경우
            departure = airlines[current].pop(0)
            visited.append((current, departure))
            current = departure
    answer = list()
    departure, arrival = visited.pop(0)
    answer.append(departure)
    answer.append(arrival)
    for _, arrival in visited:
        answer.append(arrival)
    return answer