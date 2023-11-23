def solution(s):
    Open = ["(","[","{"]
    Close = {")":"(", "]":"[", "}":"{"}
    count = 0
    
    def check (Str):
        stack = []
        
        for s in Str:
            if s in Open:
                stack.append(s)
            
            elif stack and s in Close:
                if stack[-1] == Close[s]:
                    stack.pop()
                else:
                    return 0

            elif not stack and s in Close:
                return 0
        if stack : return 0
        else : return 1
    
    for order in range(len(s)):
        Str = s[order:] + s[0:order]
        count += check(Str)
    
    return count