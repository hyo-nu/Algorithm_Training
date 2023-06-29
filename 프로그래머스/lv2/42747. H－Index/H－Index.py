def solution(citations):
    citations.sort()
    
    H_max = 0
    for H in range(1,len(citations)+1):
        h = 0
        for ct in citations:
            if H <= ct : h += 1
        if H <= h and H >= len(citations)-h: 
            H_max = max(H_max,H)
            
    return H_max