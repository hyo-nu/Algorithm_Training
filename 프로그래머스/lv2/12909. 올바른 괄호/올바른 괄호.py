def solution(s):
    stack = []
    
    for brac in s:
        if not stack :
            if brac == "(" : stack.append("(")
            else : return False
        
        else:
            if brac == "(" : stack.append("(")
            else : stack.pop()
            
    if stack : return False            
    else : return True 
    
    
    return True