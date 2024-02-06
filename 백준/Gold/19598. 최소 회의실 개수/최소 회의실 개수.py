import sys;
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
G = sorted([list(map(int, input().split())) for _ in range(N)])

h = []
room = 1
for st, et in G:
    if not h : heappush(h, et) ; continue
    if h[0] <= st: heappop(h)
    else : room += 1
    heappush(h, et)

print(room)