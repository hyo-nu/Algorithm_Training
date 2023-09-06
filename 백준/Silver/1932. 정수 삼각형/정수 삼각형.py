N = int(input())
DP = [[0]+list(map(int,input().split()))+[0] for _ in range(N)]

for r in range(1,N):
    for c in range(1,len(DP[r])-1):
        DP[r][c] += max(DP[r-1][c-1], DP[r-1][c])

print(max(map(max,DP)))