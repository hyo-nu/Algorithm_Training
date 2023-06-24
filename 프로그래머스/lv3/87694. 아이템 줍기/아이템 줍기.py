from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
        
    G = [ ['.'] * 102 for _ in range(102)]
    for r1,c1,r2,c2 in rectangle:
        for r in range(r1*2, r2*2 + 1):
            for c in range(c1*2, c2*2 + 1):
                G[r][c] = 0
    
    Q = deque()
    Q.append((characterX*2,characterY*2))
    
    def BFS():
        while Q:
            r, c = Q.popleft()
            for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < 102 and 0 <= nc < 102 and G[nr][nc] == 0 :
                    for rr, cc in ((-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)):
                        if 0 <= nr+rr < 102 and 0 <= nc+cc < 102:
                            if G[nr+rr][nc+cc] == '.':
                                Q.append((nr,nc))
                                G[nr][nc] = G[r][c] + 1
                                break                   
    BFS()                   
    return G[itemX*2][itemY*2]//2