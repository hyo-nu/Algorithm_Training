# 매일 한 가지 제품 1개 할인
# 10일 연속할인 가능한 날에 회원가입
# 회원 가입 가능한 일수 구하기
from collections import Counter

def solution(want, number, discount):
    shopping = {want[i] : number[i] for i in range(len(want))}
    result = 0
    
    for i in range(len(discount) - 9):
        if shopping == Counter(discount[i : i + 10]):
              result += 1
    
    return result