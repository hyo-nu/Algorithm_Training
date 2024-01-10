def solution(record):
    nick_dict = {}
    inout = []
    for information in record:
        state, userid, *nickname = information.split(" ")
        if state != "Leave"  : nick_dict[userid] = str(*nickname)
        if state != "Change" : inout.append((state,userid))
    answer = []
    for state, userid in inout:
        if state == "Enter" : answer.append((f'{nick_dict[userid]}님이 들어왔습니다.'))        
        elif state == "Leave" : answer.append((f'{nick_dict[userid]}님이 나갔습니다.'))        
    
    return answer