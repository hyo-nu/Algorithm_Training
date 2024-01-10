import sys
from collections import deque
input = sys.stdin.readline

def BFS(tetromino):
    global Max
    Q = set()
    while tetromino:
        r1,c1,r2,c2,r3,c3,r4,c4 = tetromino.popleft()
        Max = max(Max, G[r1][c1] + G[r2][c2] + G[r3][c3] + G[r4][c4])
        for dr, dc in ((0,1),(1,0)): # 우,하
            nr1,nc1 = r1 + dr, c1 + dc
            nr2,nc2 = r2 + dr, c2 + dc
            nr3,nc3 = r3 + dr, c3 + dc
            nr4,nc4 = r4 + dr, c4 + dc
            if 0 <= nr1 < N and 0 <= nr2 < N and 0 <= nr3 < N and 0 <= nr4 < N:
                if 0 <= nc1 < M and 0 <= nc2 < M and 0 <= nc3 < M and 0 <= nc4 < M:
                    Q.add((nr1,nc1,nr2,nc2,nr3,nc3,nr4,nc4))
                    Max = max(Max, G[nr1][nc1] + G[nr2][nc2] +G[nr3][nc3] + G[nr4][nc4])
    return Q

tetromino = deque([
    (0,0,0,1,0,2,0,3),(0,0,1,0,2,0,3,0),
    (0,0,0,1,1,0,1,1),
    (0,0,1,0,2,0,2,1),(0,2,1,0,1,1,1,2),(0,0,0,1,1,1,2,1),(0,0,0,1,0,2,1,0),
    (0,1,1,1,2,1,2,0),(0,0,0,1,0,2,1,2),(0,0,1,0,2,0,0,1),(0,0,1,0,1,1,1,2),
    (0,0,1,0,1,1,2,1),(0,1,0,2,1,0,1,1),
    (0,1,1,1,1,0,2,0),(0,0,0,1,1,1,1,2),
    (0,0,0,1,0,2,1,1),(0,0,1,0,2,0,1,1),(0,1,1,0,1,1,1,2),(1,0,0,1,1,1,2,1)])

N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
Max = 0

while tetromino:
    tetromino = deque(BFS(tetromino))
print(Max)