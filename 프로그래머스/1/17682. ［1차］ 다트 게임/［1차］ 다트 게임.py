# s,d,t 제곱수
# * : 해당점수, 바로전에점수 각 2배 (처음에 나오면 첫 점수만 2배)
# # : 해당점수 마이너스
# 

def solution(dartResult):
    dart = list(dartResult)
    score = []
    
    for i in range(len(dart)):
        if dart[i].isalpha():
            if i != 0 and dart[i-1] == "0" and dart[i-2] == "1" : num = 10
            else : num = int(dart[i-1])

        if dart[i] == "S" : score.append((num) ** 1)
        elif dart[i] == "D" : score.append((num) ** 2)
        elif dart[i] == "T" : score.append((num) ** 3)
        elif dart[i] == "*" : 
            score[-1] *= 2
            if len(score) >= 2 : score[-2] *= 2
        elif dart[i] == "#" : score[-1] *= -1
            
    
    return sum(score)