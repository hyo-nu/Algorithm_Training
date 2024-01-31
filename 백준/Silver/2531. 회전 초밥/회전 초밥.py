import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
belt = belt + belt[:k-1]

Max = 0
for i in range(N):
    fish = len(set(belt[i:i+k]))
    if c not in belt[i:i+k] : fish += 1
    Max = max(Max, fish)
print(Max)