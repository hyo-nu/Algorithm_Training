N = int(input())
DP = [1] * 10

for i in range(1,N):
    for j in range(10):
        DP[j] = sum(DP[j:])

print(sum(DP)% 10007)