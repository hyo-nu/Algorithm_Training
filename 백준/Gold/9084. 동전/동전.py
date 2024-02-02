import sys
input = sys.stdin.readline

# 1<= 테케 <=10
# 1<= 동전종류수 <= 20
# 1<= 목표금액 <= 10,000

for test in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for price in range(coin,target + 1):
            dp[price] += dp[price - coin]

    print(dp[target])