from collections import Counter

def solution(gems):
    gems_len = len(gems)
    gems_kind = {kind : 0 for kind in gems}
    zeroCnt = len(gems_kind)
    SP = EP = 0
    Min_area = 100000
    while EP <= gems_len:
        if zeroCnt:
            if EP+1 > gems_len : break
            if gems_kind[gems[EP]] == 0 : zeroCnt -= 1
            gems_kind[gems[EP]] += 1
            EP += 1
        
        elif not zeroCnt:
            if Min_area > EP-SP:
                Min_area = EP-SP
                area = [SP+1,EP]
            if gems_kind[gems[SP]] == 1 : zeroCnt += 1      
            gems_kind[gems[SP]] -= 1
            SP += 1
        
        if EP > gems_len:
            break
    return area