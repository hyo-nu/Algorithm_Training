import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
move = [
    ((0, -2), (0, -1), "W"),((-1, -2),(0, -1), "W"),                  # => 변경 후 가로
    ((-2, 0), (-1, 0), "L"),((-2, -1),(-1, 0), "L"),                  # => 변경 후 세로
    ((-1,-2), (-1,-1), "C"),((-2, -1),(-1,-1), "C"),((-2,-2),(-1,-1), "C") # => 변 경 후 대각선
]

Q = {((0, 0), (0, 1)) : 1}

for r in range(N):
    for c in range(N):
        if r == 0 and (c == 0 or c == 1) : continue
        if G[r][c] == 0:
            for dl, dr, Type in move:
                nrl, ncl = r + dl[0], c + dl[1]
                nrr, ncr = r + dr[0], c + dr[1]
                if ((nrl,ncl),(nrr,ncr)) in Q:
                    if Type == "C" and (G[r-1][c] or G[r][c-1]):continue
                    Q[(((nrr,ncr),(r,c)))] = Q.get((((nrr,ncr),(r,c))),0) + Q[((nrl,ncl),(nrr,ncr))]

Sum = 0
if ((N-1,N-2),(N-1,N-1)) in Q : Sum += Q[((N-1,N-2),(N-1,N-1))]
if ((N-2,N-1),(N-1,N-1)) in Q : Sum += Q[((N-2,N-1),(N-1,N-1))]
if ((N-2,N-2),(N-1,N-1)) in Q : Sum += Q[((N-2,N-2),(N-1,N-1))]

print(Sum)