from itertools import combinations
import sys
from itertools import combinations

N = int(input())
G, X, T = [], [], []
for R in range(N):
    tmp = list(map(str,input().split()))
    G.append(tmp)
    for C in range(N):
        if tmp[C] == "X": X.append((R,C))
        elif tmp[C] == "T": T.append((R,C))

for blocks in combinations(X,3):
    for r, c in blocks:
        G[r][c] = "O"

    meet = 0
    for r, c in T:
        for dr, dc in ((-1,0),(0,1),(1,0),(0,-1)):
            for n in range(1,N):
                nr, nc = r + dr * n, c + dc * n
                if 0 <= nr < N and 0 <= nc < N:
                    if G[nr][nc] == "O":
                        break
                    elif G[nr][nc] == "S":
                        meet += 1
                        break
            if meet : break
        if meet: break
    if not meet :
        print("YES")
        break

    for r, c in blocks:
        G[r][c] = "X"

if meet : print("NO")