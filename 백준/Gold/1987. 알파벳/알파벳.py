R, C = map(int,input().split())
G = [list(input()) for _ in range(R)]
ch = [0] * 26

def DFS(r,c,cnt):
    global Max
    Max = max(cnt,Max)

    for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc <C and ch[ord(G[nr][nc])-65] == 0:
            ch[ord(G[nr][nc]) - 65] = 1
            DFS(nr,nc,cnt+1)
            ch[ord(G[nr][nc]) - 65] = 0

Max = 1
ch[ord(G[0][0])-65] = 1
DFS(0,0,Max)

print(Max)