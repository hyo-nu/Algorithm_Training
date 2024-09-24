import sys;
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())
G = [list(input().rstrip()) for _ in range(n)]
vi = [[0] * m for _ in range(n)]
W = B = 0


def BFS(R, C, color):
    q = deque([(R, C)])
    G[R][C] = 0
    vi[R][C] = 1
    cnt = 1

    while q:
        r, c = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not vi[nr][nc] and G[nr][nc] == color:
                    q.append((nr, nc))
                    G[nr][nc] = 0
                    vi[nr][nc] = 1
                    cnt += 1
    return cnt

for r in range(n):
    for c in range(m):
        if G[r][c] == "W":
            W += BFS(r, c, "W") ** 2
        elif G[r][c] == "B":
            B += BFS(r, c, "B") ** 2

print(W, B)
