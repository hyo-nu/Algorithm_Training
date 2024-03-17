import sys;
input = sys.stdin.readline

for _ in range(int(input())):
    price = int(input())
    coins = [0] * 4

    for idx, money in enumerate((25, 10, 5, 1)):
        coins[idx] = price // money
        price %= money

    print(*coins)
