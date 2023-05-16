# 코스요리 메뉴는 2가지 이상의 단품
# 최소 2명 이상의 손님으로부터 주문
# 정답은 문자열 형식으로 배열에 담아 사전순 오름차순
from itertools import combinations 

def solution(orders, course):
    
    result = []
    for cnt in course:
        dic = {}
        tmp = []
        max = 2
        
        for order in orders:
            for item in combinations(order,cnt):
                item = ''.join(sorted(list(item)))
                
                if item not in dic : dic[item] = 1
                else : dic[item] += 1
                
        for key, value in dic.items():
            if max < value:
                max = value
                tmp = []
                tmp.append(key)
            elif value == max:
                tmp.append(key)
        result += tmp
    result.sort()
    return result