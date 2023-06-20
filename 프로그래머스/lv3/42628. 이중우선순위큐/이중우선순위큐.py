from heapq import heappop, heappush
def solution(operations):
    h = []
    for data in operations:
        ID, num = data.split()
        if ID == "I" : heappush(h, int(num))
        elif ID == "D" and h and num == "-1" : heappop(h)
        elif ID == "D" and h and num == "1" :
            h.remove(max(h))

    if not h : return [0,0]
    else : 
        return [max(h),h[0]]
