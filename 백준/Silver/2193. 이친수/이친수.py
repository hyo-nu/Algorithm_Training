import sys;
input = sys.stdin.readline

N = int(input())
DP = [[0] * 2 for _ in range(N)]
DP[0][1] = 1

for i in range(1, N):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]
    DP[i][1] = DP[i-1][0]

print(sum(DP[N-1]))