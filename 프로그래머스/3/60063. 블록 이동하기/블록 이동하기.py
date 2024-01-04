from collections import deque

def solution(board):
    N = len(board) + 2
    board = [[1] * N ] + [[1] + lst + [1] for lst in board] + [[1] * N]
    
    time = 0
    robot = deque([(1,1,1,2,0)])
    vi = [[0] * (N) for _ in range(N)]
    vi[1][1] = vi[1][2] = 1
    
    def BFS(robot):
        nonlocal time
        robot = deque(set(robot))
        Q = deque()
        route = set()
        time += 1
        
        while robot:
            r1,c1,r2,c2,status = robot.popleft() # status = > 0 : 가로, 1 : 세로

            for dr1, dc1, dr2, dc2 in ((-1,0,-1,0),(1,0,1,0),(0,-1,0,-1),(0,1,0,1)): # 이동 : 상,하,좌,우
                nr1, nc1, nr2, nc2 = r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2
                if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                    route.add((nr1,nc1,nr2,nc2))
                    if status == 0 : Q.append((nr1,nc1,nr2,nc2,0))
                    elif status == 1 : Q.append((nr1,nc1,nr2,nc2,1))
                    
                    
            if status == 0 : # 가로
                # 회전 : 왼쪽을 축으로 위
                # 회전 : 왼쪽을 축으로 아래
                # 회전 : 오른쪽을 축으로 위
                # 회전 : 오른쪽을 축으로 아래
                for idx, d in enumerate(((0,0,-1,-1),(0,0,1,-1),(-1,1,0,0),(1,1,0,0))): 
                    nr1, nc1, nr2, nc2 = r1 + d[0], c1 + d[1], r2 + d[2], c2 + d[3]
                    rotate = 0
                    if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                        if idx == 0 and board[r2-1][c2] == 0 : rotate = -1 
                        elif idx == 1 and board[r2+1][c2] == 0 : rotate = 1 
                        elif idx == 2 and board[r1-1][c1] == 0 : rotate = 1 
                        elif idx == 3 and board[r1+1][c1] == 0 : rotate = -1 

                        if rotate == 1:
                            route.add((nr1,nc1,nr2,nc2))
                            Q.append((nr1,nc1,nr2,nc2,1))

                        elif rotate == -1: 
                            route.add((nr2,nc2,nr1,nc1))
                            Q.append((nr2,nc2,nr1,nc1,1))
                
                
            elif status == 1 : # 세로
                # 회전 : 위쪽을 축으로 왼쪽
                # 회전 : 위쪽을 축으로 오른쪽
                # 회전 : 아래쪽을 축으로 왼쪽
                # 회전 : 아래쪽을 축으로 오른쪽
                for idx, d in enumerate(((0,0,-1,-1),(0,0,-1,1),(1,-1,0,0),(1,1,0,0))):
                    nr1, nc1, nr2, nc2 = r1 + d[0], c1 + d[1], r2 + d[2], c2 + d[3]
                    rotate = 0
                    if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                        if idx == 0 and board[r2][c2-1] == 0 : rotate = -1 
                        elif idx == 1 and board[r2][c2+1] == 0 : rotate = 1 
                        elif idx == 2 and board[r1][c1-1] == 0 : rotate = 1 
                        elif idx == 3 and board[r1][c1+1] == 0 : rotate = -1 

                        if rotate == 1:
                            route.add((nr1,nc1,nr2,nc2))
                            Q.append((nr1,nc1,nr2,nc2,0))

                        elif rotate == -1:
                            route.add((nr2,nc2,nr1,nc1))
                            Q.append((nr2,nc2,nr1,nc1,0))
        
        if route :
            for r1,c1,r2,c2 in route:
                vi[r1][c1] = vi[r2][c2] = 1
        
        return Q      
        
    while robot:
        robot = BFS(robot)
        if vi[N-2][N-2] : break
    
    return time