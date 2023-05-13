

def solution(priorities, location):
    Pr,Lo = priorities, location
    vi = [i for i in range(len(Pr))]
    
    cnt = 0
    check = 100
    while True:
        if Pr[0] < max(Pr):
            Pr.append(Pr.pop(0))
            vi.append(vi.pop(0))
        elif Pr[0] == max(Pr):
            cnt+=1
            Pr.pop(0)
            check = vi.pop(0)
        if check == Lo:
            break
    
    return cnt
    
            
    
        
    return vi