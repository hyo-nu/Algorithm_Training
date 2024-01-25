from itertools import permutations

def solution(expression):
    operates = set()
    for s in expression:
        if not s.isdigit() : operates.add(s)
    
    tmp = ""
    formula = []
    num_dict = {}
    for i, s in enumerate(expression):
        if s.isdigit() : tmp += s
        else :
            num_dict[chr(i+65)] = int(tmp)
            formula.append(chr(i+65))
            formula.append(s)
            tmp = ""
            
    num_dict[chr(i+65)] = int(tmp)
    formula.append(chr(i+65))
    
    Max = 0
    for case in permutations(operates):
        order = { oper : idx for idx, oper in enumerate(case,1)}
        stack = []
        answer = ""
        
        for s in formula:
            if s not in order : answer += s ; continue
            if not stack : stack.append(s)
            else:
                if order[stack[-1]] > order[s]:
                    stack.append(s)
                
                else:
                    while stack and order[stack[-1]] <= order[s]:
                        answer += stack.pop()
                    stack.append(s)
        while stack :
            answer += stack.pop()
        
        # 후위 표기식 계산
        tmp = []
        
        for value in answer:
            if value not in order:
                tmp.append(num_dict[value])
            
            else:
                b = tmp.pop()
                a = tmp.pop()
                if value == "*" : ab = a * b
                elif value == "+" : ab = a + b
                elif value == "-" : ab = a - b
                tmp.append(ab)
        Max = max(Max,abs(tmp[0]))
    
            
    return Max