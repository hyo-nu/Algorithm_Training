import sys;
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N):
    st, et = map(int,input().split())
    heappush(classes,(st,et))

rooms = []
Min = 1
for _ in range(N):
    st, et = heappop(classes)
    if rooms and st < rooms[0]:
        Min += 1
    elif rooms and st >= rooms[0]:
        heappop(rooms)
    heappush(rooms, et)
print(Min)