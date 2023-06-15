from heapq import heappop, heappush, heapify

def solution(scoville, K):
    heapify(scoville)
    count = 0
    while len(scoville) > 1:
        num1 = heappop(scoville)
        if num1 >= K: break    
        num1 += heappop(scoville) * 2 
        heappush(scoville,num1)
        count += 1
    
    if len(scoville) == 1 and scoville[0] < K : count = -1    
    return count