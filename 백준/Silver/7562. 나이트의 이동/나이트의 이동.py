from collections import deque
def BFS():
    dr = [-2,-1, 1, 2, 2, 1,-1,-2] # 우위우하좌하좌위
    dc = [ 1, 2, 2, 1,-1,-2,-2,-1]

    while Q:
        r,c = Q.popleft()
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and vi[nr][nc] == -1:
                vi[nr][nc] = vi[r][c] + 1
                Q.append((nr,nc))

Test = int(input())

for TC in range(Test):
    N = int(input())
    sr,sc = map(int,input().split())
    er,ec = map(int,input().split())
    vi  = [[-1]*N for _ in range(N)]

    Q = deque()
    Q.append((sr,sc))
    vi[sr][sc] = 0
    BFS()
    print(vi[er][ec])