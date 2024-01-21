import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
days = [list(map(int,input().split())) for _ in range(N)]
weeks = [0] * 5
Max = 0

for choice in combinations(range(5),2):
    d1, d2 = choice
    count = 0
    for i in range(N):
        if days[i][d1] and days[i][d2]:
            count += 1

    if Max <= count :
        Max = count
        for i in range(5):
            if i == d1 or i == d2 : weeks[i] = 1
            else: weeks[i] = 0

print(Max)
print(*weeks)