# 코스요리는 최소 2가지 이상의 단품
# 단품은 최소 2명 이상의 손님으로부터 주문

from itertools import combinations

def solution(orders, course):
    
    new = []
    for cnt in course:
        single = {}
        for order in orders:
            for comb in combinations(order, cnt):
                comb = "".join(sorted(comb))
                single[comb] = single.get(comb, 0) + 1
                
        single = sorted(single.items(), key = lambda x : -x[1])
        
        for idx in range(1, len(single)):
            if single[idx-1][1] >= 2 : 
                if single[idx-1][1] > single[idx][1]:
                    new.append(single[idx-1][0])
                    break
                elif single[idx-1][1] == single[idx][1]:
                    new.append(single[idx-1][0])
    
    return sorted(new)





# def solution(orders, course):
    
#     result = []
#     for cnt in course:
#         dic = {}
#         tmp = []
#         max = 2
#         for order in orders:
#             for menu in combinations(order,cnt):
#                 menu = ''.join(sorted(list(menu)))  
#                 if menu not in dic : dic[menu] = 1
#                 else : dic[menu] += 1
#         print(dic)
#         for key, value in dic.items():
#             if max < value:
#                 max = value
#                 tmp = []
#                 tmp.append(key)
#             elif value == max:
#                 tmp.append(key)
#         result += tmp
        
#     return sorted(result)