# 1 <= 유저id수 <= 8
# 1 <= 유저id길이 <= 8
#   -> 중복X, 소문자로만
# banned는 * 무조건 하나 이상 포함

def solution(user_id, banned_id):
    len_user, len_ban = len(user_id), len(banned_id)
    
    user_dict = [[] for _ in range(9)]
    for user in user_id:
        user_dict[len(user)].append(user)
    
    user_idx = { user : idx for idx, user in enumerate(user_id)}
    G = [[0] * len_ban for _ in range(len_user)]

    for idx, banned in enumerate(banned_id):
        for user in user_dict[len(banned)]:
            for i in range(len(banned)):
                if banned[i] != "*" and banned[i] != user[i]:
                    break
            else:
                G[user_idx[user]][idx] = 1
    
    vi = [[0] * len_ban for _ in range(len_user)]
    result = []

    for r in range(len_user):
        if G[r][0] == 1:
            vi[r][0] = 1
            
            def back(c, arr):
                if c == len_ban :
                    result.append(arr)
                    return
                
                for r in range(len_user):
                    if G[r][c] and sum(vi[r][:c]) < 1:
                        vi[r][c] = 1
                        back(c+1, arr + [r])
                        vi[r][c] = 0
                    
            back(1,[r])                
            vi[r][0] = 0

    real = []
    for lst in result:
        lst.sort()
        if lst not in real: real.append(lst)    
    
    
    return len(real)
