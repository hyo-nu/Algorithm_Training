# 양방향 통로
# 1번에서 각 마을로 배달

def solution(N, road, K):
    INF = int(1e9)
    G = [[INF] * (N + 1) for _ in range(N + 1)]
    
    for sp, ep, time in road:
        G[sp][ep] = min(G[sp][ep],time)
        G[ep][sp] = min(G[ep][sp],time)
    
    for n in range(1, N + 1):
        G[n][n] = 0
        
    for k in range(1, N + 1):
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if r != c:
                    G[r][c] = min(G[r][c], G[r][k] + G[k][c])
        
    deliver = 0
    for c in range(1, N + 1):
        if G[1][c] <= K : deliver += 1
    
    return deliver