# 2 <= n <= 30
# 1 <= lost <= n
# 1 <= rese <= n

def solution(n, lost, reserve):
    CL = [0] + [1] * n + [0]
    cnt = 0
    for i in range(1,n + 1):
        if i in lost : CL[i] -= 1
        if i in reserve : CL[i] += 1
    
    for i in range(1,n + 1):
        if CL[i] == 0:
            if CL[i-1] == 2: CL[i-1], CL[i] = CL[i-1] - 1, CL[i] + 1
            elif CL[i+1] == 2: CL[i+1], CL[i] = CL[i+1] -1 , CL[i] + 1        
        if CL[i] : cnt += 1    
    
    return cnt
    
