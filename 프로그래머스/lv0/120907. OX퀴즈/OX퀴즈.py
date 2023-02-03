def solution(quiz):
    
    OX_lst = []
    for q in quiz:
        one_quiz = q.split()
        
        if one_quiz[1] == '+':
            if int(one_quiz[0]) + int(one_quiz[2]) == int(one_quiz[4]):
                OX_lst.append("O")
            else:
                OX_lst.append("X")
                
        elif one_quiz[1] == '-':
            if int(one_quiz[0]) - int(one_quiz[2]) == int(one_quiz[4]):
                OX_lst.append("O")
            else:
                OX_lst.append("X")
    
    return OX_lst

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))