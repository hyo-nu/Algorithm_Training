from collections import deque

def BFS():
    global visited
    dr = [0, 1, 0,-1] # 우하좌상
    dc = [1, 0,-1, 0]
    Q = deque()
    visited = [[0] * N for _ in range(N)]
    area = 0
    num = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                num += 1
                visited[x][y] = num
                Q.append((x,y))
                area += 1
                while Q :
                    r,c = Q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N and RGB[nr][nc] == RGB[r][c]:
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = num
                                Q.append((nr,nc))
    return area
def BFS2():
    global visited
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    Q = deque()
    visited = [[0] * N for _ in range(N)]
    area = 0
    num = 0
    for x in range(N):
        for y in range(N):
            if RGB[x][y] == 'G' : RGB[x][y] = 'R'
            if visited[x][y] == 0:
                num += 1
                visited[x][y] = num
                Q.append((x, y))
                area += 1
                while Q:
                    r, c = Q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            if RGB[nr][nc] == 'G': RGB[nr][nc] = 'R'
                            if RGB[nr][nc] == RGB[r][c]:
                                if visited[nr][nc] == 0:
                                    visited[nr][nc] = num
                                    Q.append((nr, nc))
    return area
N = int(input())
RGB = [list(input()) for _ in range(N)]
print(BFS(),end = ' ')
print(BFS2())