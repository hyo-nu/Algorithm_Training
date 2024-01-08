import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    next_spot = set()
    while spot:
        now = spot.popleft()
        for dice in range(1,7):
            next = now + dice
            if next == 100 : return []
            elif next < 100 :
                if move[next] : next_spot.add(move[next])
                else : next_spot.add(next)

    return next_spot

N, M = map(int,input().split())
move = [0] * 101
for _ in range(N+M):
    before,after = map(int,input().split())
    move[before] = after

spot = deque([1])
count = 0

while spot:
    count += 1
    spot = deque(list(BFS()))

print(count)