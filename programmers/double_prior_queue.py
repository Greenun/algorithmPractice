import heapq
def solution(operations):
    h=[]
    for i in operations:
        a,b=i.split(" ")
        if a=="I":
            heapq.heappush(h,int(b))
        else:
            if len(h)>0:
                if b=="1":
                    h.pop(h.index(heapq.nlargest(1,h)[0]))
                else:
                    heapq.heappop(h)
            else:
                pass
    if len(h)==0:
        return [0,0]
    else:
        return [heapq.nlargest(1,h)[0],heapq.nsmallest(1,h)[0]]

# 본인 풀이
def solution(operations):
    import heapq
    min_queue, max_queue = list(), list()
    length = 0
    for operation in operations:        
        action, number = operation.split(' ')
        number = int(number)
        if action == "I":
            heapq.heappush(min_queue, number)
            heapq.heappush(max_queue, -1*number)
            length += 1
        else:
            if length == 0:
                continue
            if number == 1:
                value = heapq.heappop(max_queue)
            else:
                value = heapq.heappop(min_queue)
            length -= 1
            if length == 0:
                min_queue, max_queue = list(), list()
    if length == 0:
        return [0, 0]
    else:
        min_v = heapq.heappop(min_queue)
        max_v = heapq.heappop(max_queue) * -1
        return [max_v, min_v]