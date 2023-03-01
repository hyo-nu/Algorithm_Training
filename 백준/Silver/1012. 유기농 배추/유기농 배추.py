from collections import deque

def BFS():
    dr = [0, 1, 0,-1] #우하좌상
    dc = [1, 0,-1, 0]
    while Q:
        r,c = Q.pop()
        G[r][c] = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0<= nc < M and G[nr][nc] == 1:
                Q.append((nr, nc))

Test = int(input())

for TC in range(Test):
    M, N, K = map(int,input().split())
    G = [[0] * (M) for _ in range(N)]
    Q = deque()
    result = 0
    for _ in range(K):
        y,x = map(int,input().split())
        G[x][y] = 1

    for r in range(N):
        for c in range(M):
            if G[r][c] == 1:
                Q.append((r,c))
                BFS()
                result += 1
    print(result)