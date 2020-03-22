def solution(n, t, m, timetable):
    import datetime
    import heapq
    bus_time = datetime.datetime.strptime("09:00", "%H:%M")    
    bus_schedule = list()
    time_queue = list()
    
    for _ in range(n):
        bus_schedule.append(bus_time)
        bus_time += datetime.timedelta(minutes=t)
    
    # 문제 조건과 다르게 24:00 이 있어서 에러가 발생 ㅡㅡ
    for tt in timetable:
        try:
            heapq.heappush(time_queue, datetime.datetime.strptime(tt, "%H:%M"))
        except:
            pass
        
    last_bus = bus_schedule[-1]
    for i, bus in enumerate(bus_schedule):        
        last_rode = list()
        for _ in range(m):
            if len(time_queue) == 0:
                return datetime.datetime.strftime(last_bus, "%H:%M")
            passenger = time_queue[0]
            if passenger <= bus:
                heapq.heappop(time_queue)
                last_rode.append(passenger)
            else:
                break
    if len(last_rode) < m:
        return datetime.datetime.strftime(last_bus, "%H:%M")
    else:
        last_passenger = last_rode[-1]
        return datetime.datetime.strftime(last_passenger - datetime.timedelta(minutes=1), "%H:%M")
    
    