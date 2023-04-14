from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x > 0 : heappush(h,x)
    else :
        if h : print(heappop(h))
        else : print(0)