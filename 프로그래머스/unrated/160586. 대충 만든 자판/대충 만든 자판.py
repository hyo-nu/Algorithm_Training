def solution(keymap, targets):
    answer = 1000
    for idx,target in enumerate(targets):
        count = 0
        for tar in target:
            Min = 999999
            for key in keymap:
                for i,k in enumerate(key):
                    if tar == k and Min > i+1:
                        Min = i+1
                        break
            if Min != 999999:
                count += Min
            else : break
        if Min != 999999:
            targets[idx] = count
        else : targets[idx] = -1
                     
        
    return targets

