def solution(age):
    
    alpa = ['a','b','c','d','e','f','g','h','i','j']
    
    answer_f = ''
    answer = ''
    
    while age != 0:
        answer_f = answer_f + alpa[age % 10]
        age = age // 10 
    
    for c in range(len(answer_f),0,-1):
        answer = answer + answer_f[c-1]
        
    return answer