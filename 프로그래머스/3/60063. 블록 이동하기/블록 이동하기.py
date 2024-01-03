from collections import deque

def solution(board):
    time = 0  
    N = len(board)
    robot = deque([(0,0,0,1,0)])
    vi = [[0] * N for _ in range(N)]
    vi[0][0] = vi[0][1] = 1
    
    
    def BFS(robot):
        nonlocal time
        robot = deque(set(robot))
        Q = deque()
        route = set()
        time += 1

        while robot:
            r1,c1,r2,c2,status = robot.popleft() # status = > 0 : 가로, 1 : 세로
            if status == 0 : # 가로
                for dr1, dc1, dr2, dc2 in ((-1,0,-1,0),(1,0,1,0),(0,-1,0,-1),(0,1,0,1)): # 이동 : 상,하,좌,우
                    nr1, nc1, nr2, nc2 = r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2
                    if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                        if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                            route.add((nr1,nc1,nr2,nc2))
                            Q.append((nr1,nc1,nr2,nc2,0))
                    
                for idx, d in enumerate(((0,0,-1,-1),(0,0,1,-1),(-1,1,0,0),(1,1,0,0))): # 회전 : 왼쪽위,왼쪽아래,오른쪽위,오른쪽아래
                    nr1, nc1, nr2, nc2 = r1 + d[0], c1 + d[1], r2 + d[2], c2 + d[3]
                    rotate = 0
                    if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                        if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                            if idx == 0 and 0 <= r2-1 < N and board[r2-1][c2] == 0 : rotate = -1 
                            elif idx == 1 and 0 <= r2+1 < N and board[r2+1][c2] == 0 : rotate = 1 
                            elif idx == 2 and 0 <= r1-1 < N and board[r1-1][c1] == 0 : rotate = 1 
                            elif idx == 3 and 0 <= r1+1 < N and board[r1+1][c1] == 0 : rotate = -1 
                                
                            if rotate == 1:
                                route.add((nr1,nc1,nr2,nc2))
                                Q.append((nr1,nc1,nr2,nc2,1))

                            elif rotate == -1: 
                                route.add((nr2,nc2,nr1,nc1))
                                Q.append((nr2,nc2,nr1,nc1,1))
                
                
            elif status == 1 : # 세로
                for dr1, dc1, dr2, dc2 in ((-1,0,-1,0),(1,0,1,0),(0,-1,0,-1),(0,1,0,1)): # 이동 : 상,하,좌,우
                    nr1, nc1, nr2, nc2 = r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2
                    if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                        if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                            route.add((nr1,nc1,nr2,nc2))
                            Q.append((nr1,nc1,nr2,nc2,1))
                
                for idx, d in enumerate(((0,0,-1,-1),(0,0,-1,1),(1,-1,0,0),(1,1,0,0))): # 회전 : 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
                    nr1, nc1, nr2, nc2 = r1 + d[0], c1 + d[1], r2 + d[2], c2 + d[3]
                    rotate = 0
                    if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                        if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                            if idx == 0 and 0 <= c2-1 < N and board[r2][c2-1] == 0 : rotate = -1 
                            elif idx == 1 and 0 <= c2+1 < N and board[r2][c2+1] == 0 : rotate = 1 
                            elif idx == 2 and 0 <= c1-1 < N and board[r1][c1-1] == 0 : rotate = 1 
                            elif idx == 3 and 0 <= c1+1 < N and board[r1][c1+1] == 0 : rotate = -1 

                            if rotate == 1:
                                route.add((nr1,nc1,nr2,nc2))
                                Q.append((nr1,nc1,nr2,nc2,0))

                            elif rotate == -1:
                                route.add((nr2,nc2,nr1,nc1))
                                Q.append((nr2,nc2,nr1,nc1,0))
        
        if route :
            for r1,c1,r2,c2 in route:
                vi[r1][c1] = vi[r2][c2] = 1
        
        # print("시간 : ",time)
        # print(Q)
        # for lst in vi:
        #     print(lst)
        return Q      
    # print("---------보드---------")
    # for lst in board:
    #     print(lst)
    # print("---------보드---------")
        
    while robot:
        robot = BFS(robot)
        if vi[N-1][N-1] : break
    
    return time