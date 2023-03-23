from collections import deque

def solution(maps):
    N = 0
    
    for i in maps:
        M = len(i)
        N += 1
    Q = deque()
    Q.append((0,0))
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    maps[0][0] = 2
    
    while Q:
        r,c = Q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <=nr < N and 0 <= nc <M and maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1
                Q.append((nr,nc))
                         
    if maps[N-1][M-1] != 1:
        answer = maps[N-1][M-1]-1
    else: 
        answer = -1
    
    return answer