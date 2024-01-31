import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
belt = belt + belt[:k-1]
kind = [0] * (d + 1)


fishRice = 0
for i in range(k):
    if not kind[belt[i]]:
        fishRice += 1
    kind[belt[i]] += 1

Max = fishRice
if not kind[c]: Max += 1

for ep in range(k, N + k - 1):
    sp = ep - k
    kind[belt[sp]] -= 1
    if not kind[belt[sp]] : fishRice -= 1

    if not kind[belt[ep]] :
        fishRice += 1
    kind[belt[ep]] += 1

    if not kind[c] : Max = max(Max, fishRice + 1)
    else : Max = max(Max, fishRice)

print(Max)