# 닉네임 변경방법 
 # 채팅방을 나간 후 새로운 닉네임으로 재 입장
 # 채팅방에서 닉네임 변경
# 닉네임 변경 시 기존 채팅방에 메시지 닉네임도 변경
# 닉네임 중복을 허용



def solution(record):
    userinfo = {}
    chat = []
    result = []
    for re in record:
        state, ID, *nick = re.split(" ")
        if state == "Enter": 
            userinfo[ID] = str(*nick)
            chat.append(("Enter",ID))
        elif state == "Leave":
            chat.append(("Leave", ID))
        else :
            userinfo[ID] = str(*nick)
            
    for i in range(len(chat)):
        if chat[i][0]== "Enter": chat[i] = f'{userinfo[chat[i][1]]}님이 들어왔습니다.'
        else : chat[i] = f'{userinfo[chat[i][1]]}님이 나갔습니다.'
            
    return chat

# def solution(record):
#     nick_dict = {}
#     inout = []
#     for information in record:
#         state, userid, *nickname = information.split(" ")
#         if state != "Leave"  : nick_dict[userid] = str(*nickname)
#         if state != "Change" : inout.append((state,userid))
#     answer = []
#     for state, userid in inout:
#         if state == "Enter" : answer.append((f'{nick_dict[userid]}님이 들어왔습니다.'))        
#         elif state == "Leave" : answer.append((f'{nick_dict[userid]}님이 나갔습니다.'))        
    
#     return answer