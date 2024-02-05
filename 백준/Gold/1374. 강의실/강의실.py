import sys;
from heapq import heappop, heappush
input = sys.stdin.readline

# 시작 순으로 정렬해서 확인

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort(key = lambda x : x[1])

rooms = []
Min = 1
for i in range(N):
    num, st, et = classes[i]
    if rooms and st < rooms[0]:
        Min += 1
    elif rooms and st >= rooms[0]:
        heappop(rooms)
    heappush(rooms, et)
print(Min)