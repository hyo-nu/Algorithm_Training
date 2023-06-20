from heapq import heappop, heappush

def solution(operations):
    h = []
    for data in operations:
        ID, num = data.split()
        if ID == "I" : heappush(h, int(num))
        elif ID == "D" and h and num == "-1" : heappop(h)
        elif ID == "D" and h and num == "1" :
            tmp = [-heappop(h) for _ in range(len(h))]
            tmp.sort(reverse = True)
            tmp.pop()
            for ele in tmp:
                heappush(h,-ele)               
    if not h : return [0,0]
    else : 
        h.sort()
        return [h[-1],h[0]]
