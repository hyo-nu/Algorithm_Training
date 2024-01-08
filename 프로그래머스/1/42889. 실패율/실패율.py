# 스테이지 도달 but 클리어 no / 스테이지 도달
# N : 전체 스테이지
# stages : 사용자의 현재 위치
# 실패율 높은 순으로 정렬

def solution(N, stages):
    stop = [0] * (N + 2)
    for stage in stages: stop[stage] += 1
    
    fail = []
    player = len(stages)
    for i in range(1, N+1):
        if player == 0 : fail.append((0,i)) ; continue
        fail.append(((stop[i] / player),i))
        player -= stop[i]
        
    fail.sort(key = lambda x:-x[0])
    print(fail)
    
    return [stage for _,stage in fail]


# def solution(N, stages):
#     stages.sort()
#     down = len(stages)
#     result = []
#     for i in range(1, N + 1):
#         if down != 0:
#             up = stages.count(i)
#             fail = up / down
#             result.append((fail,i))
#             down -= up
#         else : result.append((0,i))
#     result.sort(key = lambda x : -x[0])
    
#     for i in range(N):
#         result[i] = result[i][1]
#     return result

# def solution(N, stages):
#     percent_lst = []
#     answer = []

#     for i in range(1,N+1):
#         total = retire = 0

#         for j in stages:
#             if j >= i : 
#                 total += 1
#                 if j == i : retire += 1
#         try:      
#             percent_lst.append([i,retire/total])     
#         except: percent_lst.append([i,0])

#     percent_lst.sort(key = lambda x : x[1],reverse = True)

#     for num,per in percent_lst:
#         answer.append([num,per])
#     return answer
