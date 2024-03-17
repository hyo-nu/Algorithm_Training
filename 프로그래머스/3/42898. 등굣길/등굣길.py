def solution(m, n, puddles):
    INF = 1_000_000_007
    G = [[0] * (m+1) for _ in range(n+1)]
    for r,c in puddles : G[c][r] = INF
    G[1][1] = 1
    
    for r in range(n + 1):
        for c in range(m + 1):
            if G[r][c] != INF:
                if G[r-1][c] != INF : G[r][c] += G[r-1][c]
                if G[r][c-1] != INF : G[r][c] += G[r][c-1]
    
    for lst in G:print(lst)
    
    return G[n][m] % INF

# def solution(m, n, puddles):
#     G = [[0] * m for _ in range(n)]
#     for r, c in puddles:
#         G[c-1][r-1] = '*'
#     G[0][0] = 1
    
#     for r in range(n):
#         for c in range(m):
#             if G[r][c] != "*":
#                 for dr,dc in ((1,0),(0,1)):
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < n and 0 <= nc < m and G[nr][nc] != '*':
#                         G[nr][nc] += G[r][c]
#     for lst in G:
#         print(lst)
    
#     return G[n-1][m-1] % 1000000007