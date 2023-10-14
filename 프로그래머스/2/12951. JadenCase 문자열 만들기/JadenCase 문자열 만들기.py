def solution(s):
    answer = []
    lst = list(s.split(" "))
    
    
    for el in lst:
        if el and el[0].isdigit(): 
            tmp = el[0] + el[1:].lower()
            answer.append(tmp)
        elif el and not el[0].isdigit() :
            tmp = el[0].upper() + el[1:].lower()
            answer.append(tmp)
        else : 
            answer.append("")
    
    return " ".join(answer)

