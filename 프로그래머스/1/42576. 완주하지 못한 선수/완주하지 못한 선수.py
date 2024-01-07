def solution(participant, completion):
    dict = {}
    for part in participant:
        if part in dict : dict[part] += 1
        else: dict[part] = 1
    
    for com in completion:
        dict[com] -= 1
    
    for who, value in dict.items():
        if value != 0 :
            return who
        
    return 0