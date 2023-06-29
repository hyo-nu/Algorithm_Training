def solution(m, n, puddles):
    G = [[0] * m for _ in range(n)]
    for r, c in puddles:
        G[c-1][r-1] = '*'
    G[0][0] = 1
    
    for r in range(n):
        for c in range(m):
            if G[r][c] != "*":
                for dr,dc in ((1,0),(0,1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and G[nr][nc] != '*':
                        G[nr][nc] += G[r][c]
    for lst in G:
        print(lst)
    
    return G[n-1][m-1] % 1000000007