import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
relst = lst[::-1]
dp, redp = [1] * N, [1] * N

for i in range(1,N):
    for j in range(i):
        if lst[i] > lst[j] : dp[i] = max(dp[i], dp[j] + 1)
        if relst[i] > relst[j] : redp[i] = max(redp[i], redp[j] + 1)

logest = 0
for i in range(N):
    logest = max(logest, dp[i] + redp[N-i-1])

print(logest-1)