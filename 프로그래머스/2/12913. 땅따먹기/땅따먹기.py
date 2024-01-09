def solution(land):
    N = len(land)
    for nr in range(1, N):
        for nc in range(4):
            Max = 0
            for bc in range(4):
                if nc != bc :
                    Max = max(Max, land[nr-1][bc])
            land[nr][nc] += Max
    
    return max(land[N-1])