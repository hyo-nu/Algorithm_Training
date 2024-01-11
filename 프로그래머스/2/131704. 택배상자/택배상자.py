def solution(order):
    sub, main = [], 1
    move = 0
    while move < len(order):
        if not sub : 
            sub.append(main)
            main += 1
        elif order[move] != sub[-1]:
            if order[move] > sub[-1]:
                sub.append(main)
                main += 1
            else : break
        else :
            sub.pop()
            move += 1
    return move


