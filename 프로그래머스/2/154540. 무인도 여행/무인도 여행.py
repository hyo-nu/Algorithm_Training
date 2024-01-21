from collections import deque

def solution(maps):
    maps = list(map(list,maps))
    N, M = len(maps), len(maps[0])
    
    def BFS(r,c):
        Q = deque([(r,c)])
        days = int(maps[r][c])
        maps[r][c] = "X"
        while Q:
            r, c = Q.popleft()
            for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and maps[nr][nc].isdigit():
                    Q.append((nr,nc))
                    days += int(maps[nr][nc])
                    maps[nr][nc] = "X"
        
        return days

    result = []
    for r in range(N):
        for c in range(M):
            if maps[r][c].isdigit():
                days = BFS(r,c)
                if days : result.append(days)
    
    return sorted(result) if result else [-1]