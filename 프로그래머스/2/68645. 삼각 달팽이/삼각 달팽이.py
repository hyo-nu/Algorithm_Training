import math

def solution(n):
    G = [[0] * i for i in range(1, n + 1)]
    vi = [[0] * i for i in range(1, n + 1)]
    
    r, c, order = -1, 0, 1
    stop = sum([i for i in range(1,n+1)])
    while order <= stop:
        for dr, dc in ((1,0),(0,1),(-1,-1),(0,-1)): #아래,오른,위,왼
            while True:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < len(G[nr]) and not vi[nr][nc]:
                    G[nr][nc] = order
                    vi[nr][nc] = 1
                    r, c = nr, nc
                    order += 1
                else : break
    
    answer = []
    for lst in G:answer.extend(lst)
    return answer