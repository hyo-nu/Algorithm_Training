import sys
import math

input = sys.stdin.readline

n = int(input())
scores = sorted([int(input()) for _ in range(n)])
cut = math.floor(n * 0.15 + 0.5)
print(math.floor((sum(scores[cut : n - cut]) / (n - cut * 2)) + 0.5) if n else 0)