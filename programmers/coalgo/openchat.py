def solution(record):
    action_map = {
        "Enter": enter_handler,
        "Leave": leave_handler,
        "Change": change_handler,
    }
    nickname_map = dict()
    history = list()
    for line in record:
        cmd = line.split(' ')
        action = cmd[0]
        action_map[action](history, nickname_map, cmd[1:])
    for i in range(len(history)):
        uid, log = history[i].split('-')
        history[i] = nickname_map[uid] + log
    return history
        
    
def enter_handler(history, nickname_map, *args):
    uid, nickname = args[0]
    history.append(uid+"-님이 들어왔습니다.")
    nickname_map[uid] = nickname
    
def leave_handler(history, nickname_map, *args):
    # print("leave: ", args[0])
    uid = args[0][0]
    history.append(uid+"-님이 나갔습니다.")

def change_handler(history, nickname_map, *args):
    # print("change: ", args)
    uid, nickname = args[0]
    nickname_map[uid] = nickname
