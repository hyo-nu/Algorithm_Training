import sys
from heapq import heappush, heappop
input = sys.stdin.readline

for test in range(int(input())):
    k = int(input())
    hmax, hmin = [], []
    hash_max, hash_min = {}, {}
    insert_cnt = delete_cnt = 0

    for _ in range(k):
        ID, num = input().split()
        if ID == "I":
            insert_cnt += 1
            heappush(hmax, -int(num))
            heappush(hmin, int(num))

        elif ID == "D" and insert_cnt > delete_cnt:
            delete_cnt += 1

            if hmax and num == "1":
                Max = heappop(hmax)
                hash_max[Max] = hash_max.get(Max, 0) + 1

            elif hmin and num == "-1":
                Min = heappop(hmin)
                hash_min[Min] = hash_min.get(Min, 0) + 1

        while hmax and -hmax[0] in hash_min and hash_min[-hmax[0]] > 0:
            hash_min[-hmax[0]] -= 1
            heappop(hmax)

        while hmin and -hmin[0] in hash_max and hash_max[-hmin[0]] > 0:
            hash_max[-hmin[0]] -= 1
            heappop(hmin)

    print(f"{-heappop(hmax)} {heappop(hmin)}" if hmax and hmin else "EMPTY")