# 12번 실패 e.g., cdcde, cdcdcde
def solution(m, musicinfos):
    import re
    import datetime
    match = None
    match_play = 0
    for mi in musicinfos:
        start, end, name, melody = mi.split(',')
        start = datetime.datetime.strptime(start, "%H:%M")
        end = datetime.datetime.strptime(end, "%H:%M")
        play_time = int((end - start).total_seconds() // 60)
        extended = extend_melody(melody_to_list(melody), play_time)
        if subset(extended, melody_to_list(m)):
            if match_play < play_time:
                match = name
                match_play = play_time
    if not match:
        return "(None)"
    else:
        return match
    
        
        
def extend_melody(melody: list, play_time):
    length = len(melody)
    if length >= play_time:
        return melody[:play_time]
    else:
        new_melody = list()
        repeat = play_time // length
        mod = play_time % length 
        new_melody = melody*repeat
        new_melody.extend(melody[:mod])
        return new_melody

def melody_to_list(melody):
    melody_list = list()
    temp = ""
    for m in melody:
        if m == "#":
            melody_list.append(temp + m)
            temp = ""
        else:
            if temp:
                melody_list.append(temp)
                temp = m
            else:
                temp += m
    if temp: melody_list.append(temp)
    return melody_list

def subset(origin, sub):
    includes = list()
    i = 0
    for o in origin:
        if i >= len(sub): break
        if o == sub[i]:
            i += 1
            includes.append(o)
        else:
            i = 0
            includes = list()
    if includes == sub:
        return True
    else:
        return False


# 통과

def solution(m, musicinfos):
    import re
    import datetime
    match = None
    match_play = 0
    for mi in musicinfos:
        start, end, name, melody = mi.split(',')
        start = datetime.datetime.strptime(start, "%H:%M")
        end = datetime.datetime.strptime(end, "%H:%M")
        play_time = int((end - start).total_seconds() // 60)
        extended = extend_melody(melody_to_list(melody), play_time)
        if subset(extended, melody_to_list(m)):
            if match_play < play_time:
                match = name
                match_play = play_time
    if not match:
        return "(None)"
    else:
        return match
    
        
        
def extend_melody(melody: list, play_time):
    length = len(melody)
    if length >= play_time:
        return melody[:play_time]
    else:
        new_melody = list()
        repeat = play_time // length
        mod = play_time % length 
        new_melody = melody*repeat
        new_melody.extend(melody[:mod])
        return new_melody

def melody_to_list(melody):
    melody_list = list()
    temp = ""
    for m in melody:
        if m == "#":
            melody_list.append(temp + m)
            temp = ""
        else:
            if temp:
                melody_list.append(temp)
                temp = m
            else:
                temp += m
    if temp: melody_list.append(temp)
    return melody_list

def subset(origin, sub):
    includes = list()
    for i in range(len(origin) - len(sub) + 1):
        temp = i
        for j in range(len(sub)):
            if origin[temp] == sub[j]:
                includes.append(origin[temp])
                temp += 1
            else:
                includes.clear()
                break
        if includes == sub:
            return True
    return False

# 다른 더 깔끔한 풀이
def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
    music_dic = dict()
    answer = ["",""]
    for information in musicinfos:
        start, end, name, music = information.split(',')
        music = music.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
        start =[int(time) for time in start.split(':')]
        end = [int(time) for time in end.split(':')]
        all_time = (end[0]-start[0])*60 + (end[1]-start[1])
        music = music*(all_time//len(music)) + music[0:all_time%len(music)]
        music_dic[name] = music
    for key,value in music_dic.items():
        if m in value:
            if len(answer[1]) < len(value): 
                answer[0] = key
                answer[1] = value
    return "(None)" if len(answer[0]) == 0 else answer[0]