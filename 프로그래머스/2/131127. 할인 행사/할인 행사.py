# 매일 한 가지 제품 1개 할인
# 10일 연속할인 가능한 날에 회원가입
# 회원 가입 가능한 일수 구하기

def solution(want, number, discount):
    shopping = {want[i] : number[i] for i in range(len(want))}
    
    result = 0
    for day in range(len(discount) - 9):
        salse = {}
        for i in range(10):
            if discount[day + i] not in salse : salse[discount[day + i]] = 1
            else : salse[discount[day + i]] += 1
        for item, cnt in salse.items():
            if item not in shopping: break
            elif cnt > shopping[item] : break
        else:
            result += 1
    return result