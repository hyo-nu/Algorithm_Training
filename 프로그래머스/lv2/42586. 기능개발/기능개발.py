def solution(progresses, speeds):
    
    lst = []
    answer = []
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i] == 0:
            lst.append((100 - progresses[i]) // speeds[i])
        else:lst.append(((100 - progresses[i]) // speeds[i])+1)

    cnt = 1
    lst.append(-1)
    Max = lst[0]
    for i in range(len(lst)-1):
        if lst[i+1] > 0:
            if Max < lst[i+1]:
                answer.append(cnt)
                Max = lst[i+1]
                cnt = 1
            else: cnt += 1
        else:answer.append(cnt)        
    return answer