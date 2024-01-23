# MBTI 같음 16개의 성격유형
# n 개의 질문, 7개의 선택지
# 선택지에 따른 유형 점수가 존재함
# 점수를 더 많이 받은 유형으로 채택
# 점수 같으면? 유형의 사전 순
# survey의 첫번째 :: 비동의
# survey의 두번쨰 :: 동의

def solution(survey, choices):
    type_score = {}
    character = ""
    
    for idx, el in enumerate(survey):
        disagree, agree = el[0], el[1]
        
        # 비동의 점수 획득
        if choices[idx] < 4:
            score = 4 - choices[idx]
            type_score[disagree] = type_score.get(disagree, 0) + score
            
        # 동의 점수 획득
        elif choices[idx] > 4:
            score = choices[idx] - 4
            type_score[agree] = type_score.get(agree, 0) + score
        
    
    for type1, type2 in (("R","T"),("C","F"),("J","M"),("A","N")):
        score1 = type_score.get(type1, 0)
        score2 = type_score.get(type2, 0)
        
        if score1 >= score2 : character += type1
        elif score1 < score2 : character += type2
        
    
    return character




