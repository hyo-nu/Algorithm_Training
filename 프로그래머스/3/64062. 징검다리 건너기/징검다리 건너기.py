# # 디딤돌은 밟으면 숫자 -1
# # 0이면 못 밟음, k칸 점프 가능
# # 점프는 무조건 가장 가까은 돌
# # 동시에 못 건넘

import heapq
from math import inf

def solution(stones, k):
    n = len(stones)

    queue = []
    answer = inf

    for i in range(k - 1):
        heapq.heappush(queue, [-stones[i], i])
        
    for i in range(k - 1, n):
        heapq.heappush(queue, [-stones[i], i])
        while queue[0][1] < i - k + 1:
            tmp = heapq.heappop(queue)
        answer = min(answer, -queue[0][0])

    return answer


# from heapq import heappop, heapify, heappush

# def solution(stones, k):
#     sp, jump = 0, k
#     Min = Max = max(stones[:k])
#     h = []
#     for i in range(k):
#         heappush(h,(-stones[i],i))
    
#     for i in range(k, len(stones)):
#         Max = max(Max,stones[i])
#         heappush(h,(-stones[i],i))
#         sp += 1
#         if stones[sp-1] == Max:
#             tmp = []
#             while True:
#                 Max, idx = heappop(h)
#                 if idx > sp - 1 : break
#             Min = min(Min, -Max)
            
#     return Min

