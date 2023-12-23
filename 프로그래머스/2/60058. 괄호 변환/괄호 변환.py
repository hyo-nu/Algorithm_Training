# 균형 -> 올바른
# 이미 볼바르다면 그대로 return
# w를 균형u, 균형v로 분리 (u는 분리 불가, v는 빈 문자열 가능)
# u가 올바르면 
    # v에 대해 첨부터 다시
    # 결과를 u에 붙혀 반환
# u가 올바르지 않으면
    # 빈 문자열에 ( 추가
    # v에 대해 첨부터 다시 수행
    # ) 추가
    # u의 처음 마지막 제거, 나머지 문자 뒤집어서 이어 붙힘
    # 문자열 반환

def solution(p):
    Open = Close = 0
    isTrue = True
    
    for i in range(len(p)):
        if p[i] == "(" : Open += 1
        elif p[i] == ")" : Close += 1
        
        if Close > Open : isTrue = False
        
        if Open == Close : # 균형, u v 분리
            u = p[: i + 1]
            if len(p) > i + 1:
                v = p[i + 1:]
                v = solution(v)
            else : v = ""
            break
    
    if isTrue:
        
        ans = u + v
    else:
        ans = "(" + v + ")"
        for i in u[1 : -1]:
            if i == "(" : 
                ans += ")"
            else:
                ans += "("
    
    return ans
    