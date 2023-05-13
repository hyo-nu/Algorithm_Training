from collections import Counter

def solution(k, tangerine):
    dic = Counter(tangerine)
    lst = sorted(list(dic.values()))    
    lst.sort(reverse = True)
    
    choice = Type = 0
    for cnt in lst:
        choice += cnt
        Type += 1
        if choice >= k:
            break 

    return Type