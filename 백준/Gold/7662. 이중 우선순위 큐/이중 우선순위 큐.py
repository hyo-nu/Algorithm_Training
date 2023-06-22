import sys
from heapq import heappop, heappush

input = sys.stdin.readline

Test = int(input())


for TC in range(Test):
    K = int(input())
    min_h, max_h = [], []
    vi = [0] * K

    for k in range(K):
        ID, num = map(str, input().split())
        if ID == "I":
            heappush(min_h, (int(num),k))
            heappush(max_h, (-int(num),k))
            vi[k] = 1
        else:
            if num == "-1":
                while min_h and not vi[min_h[0][1]]: heappop(min_h)
                if min_h: vi[heappop(min_h)[1]] = 0
            elif num == "1":
                while max_h and not vi[max_h[0][1]]: heappop(max_h)
                if max_h: vi[heappop(max_h)[1]] = 0

        while min_h and not vi[min_h[0][1]]: heappop(min_h)
        while max_h and not vi[max_h[0][1]]: heappop(max_h)

    if min_h :
        print(-max_h[0][0], min_h[0][0])
    else:
        print("EMPTY")