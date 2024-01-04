while True:
    stack = []
    sentence = input()
    if sentence == "." : break

    for alpha in sentence:
        if alpha == "(" or alpha == "[" : stack.append(alpha)
        elif alpha == ")":
            if stack and stack[-1] == "(" : stack.pop()
            else : print("no") ; break

        elif alpha == "]":
            if stack and stack[-1] == "[" : stack.pop()
            else : print("no") ; break
    else:
        print("yes") if not stack else print("no")