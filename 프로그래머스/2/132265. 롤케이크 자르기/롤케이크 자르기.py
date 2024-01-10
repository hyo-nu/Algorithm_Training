def solution(topping):
    answer = -1
    cut = 0
    left, right = {}, {}
    for i in range(len(topping)):
        right[topping[i]] = right.get(topping[i],0) + 1
    
    for i in range(len(topping)):
        left[topping[i]] = left.get(topping[i],0) + 1
        right[topping[i]] -= 1
        if right[topping[i]] == 0 : right.pop(topping[i])
        if len(left) !=0 and len(left) == len(right) : cut += 1
    return cut