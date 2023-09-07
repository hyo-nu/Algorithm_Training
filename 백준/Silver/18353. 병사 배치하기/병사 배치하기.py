N =  int(input())
lst = [10**7] + list(map(int,input().split()))
DP = [0] * (N + 1)

for i in range(1, N + 1):
    mn = 0
    for j in range(0,i):
        if lst[j] > lst[i]:
            mn = max(mn,DP[j])
    DP[i] = mn + 1
print(N-max(DP))