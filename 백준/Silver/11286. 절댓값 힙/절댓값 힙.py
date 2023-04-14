import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x != 0 : heappush(h,(abs(x),x))
    else :
        if h : print(heappop(h)[1])
        else : print(0)