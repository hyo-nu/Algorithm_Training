from itertools import permutations

def solution(n, weak, dist):
    INF = int(1e9)
    Len_weak = len(weak)
    weak = weak + [w + n for w in weak]
    Min = INF
    for sp in range(Len_weak):
        for case in permutations(dist, len(dist)):
            cnt = 1
            Now = sp
            for i in range(1, Len_weak):
                Next = sp + i
                diff = weak[Next] - weak[Now]
                if diff > case[cnt - 1]:
                    Now = Next
                    cnt += 1
                    if cnt > len(dist) : break
            if cnt <= len(dist):
                Min = min(Min, cnt)
    
    if Min == INF:
        return -1
    return Min