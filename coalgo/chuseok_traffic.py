def solution(lines):
    start_time = list()
    end_time = list()
    for line in lines:
        st, ed = to_seconds(line)
        start_time.append(st)
        end_time.append(ed)
    
    max_pps = 0
    for i in range(len(start_time)):
        for k in range(2):
            pps = 0
            start_point = start_time[i] if k == 0 else end_time[i]
            end_point = start_point + 999
            for j in range(len(start_time)):
                if (start_point <= start_time[j] <= end_point) or (start_point <= end_time[j] <= end_point) or (start_time[j] <= start_point <= end_time[j]) or (start_time[j] <= end_point <= end_time[j]):
                    pps += 1
            # print(start_point, pps, start_time[j], end_time[j], end_point)
            if max_pps < pps:
                max_pps = pps
    return max_pps
                
        
def to_seconds(datestamp):
    _, timestamp, elapsed = datestamp.split(' ')[:3]
    hours, minutes, seconds = timestamp.split(":")
    
    total = 3600*int(hours)*1000 + 60*int(minutes)*1000 + float(seconds)*1000
    
    return total - 1000*float(elapsed[:-1]) + 1, total
    
