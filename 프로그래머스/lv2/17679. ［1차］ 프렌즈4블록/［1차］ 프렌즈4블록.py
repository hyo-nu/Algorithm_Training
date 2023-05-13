from collections import deque

def solution(m, n, board):
    
    
    def find():
        Q = deque()
        cnt = 0
        for r in range(m):
            for c in range(n):
                if board[r][c]:
                    for dr, dc in ((0,1),(1,1),(1,0)):#우하좌
                        mr, mc = r + dr, c + dc
                        if mr < 0 or mr >= m or mc < 0 or mc >= n or board[r][c] != board[mr][mc]: 
                            break
                    else:
                        for dr, dc in ((0,0),(0,1),(1,1),(1,0)):#우 하 좌 상            
                            nr, nc = r + dr, c + dc
                            Q.append((nr,nc))
        Q = set(Q)
        while Q:
            r,c = Q.pop()
            board[r][c] = 0
            cnt += 1
            
        return cnt
    
    def arrange():
        for C in range(n):
            for R in range(m-1,0,-1):
                if not board[R][C]:
                    for i in range(R-1,-1,-1):
                        if board[i][C]:
                            board[R][C], board[i][C] = board[i][C],board[R][C]
                            break
                
    for mm in range(m):
        board[mm] = list(board[mm])
        
    answer = 0
    
    while True :
        tmp = find()
        if not tmp : break
        answer += tmp
        arrange()
        print()
        
        
    return answer
    
