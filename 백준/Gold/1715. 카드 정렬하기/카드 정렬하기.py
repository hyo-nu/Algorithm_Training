from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
heapify(cards)

result = 0
while len(cards) > 1:
    a = heappop(cards)
    b = heappop(cards)
    result = result + a + b
    heappush(cards,a+b)

print(result)