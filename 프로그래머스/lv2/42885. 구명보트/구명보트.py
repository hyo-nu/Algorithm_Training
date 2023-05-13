# 한번에 2명
# 1 <= 사람 <= 50,000
# 40 <= 몸무게 <=240
# 40 <= 보트 <= 240

def solution(people, limit):
    p = sorted(people)
    SP, EP = 0 , len(people) - 1 
    boat = over = 0  
    # boat = 보트수
    # over = 몸무게 초과인지 아닌지
    
    while SP < EP:
        if p[SP] + p[EP] > limit : over = 1
        else : over, SP = 0, SP + 1        
        EP ,boat = EP - 1, boat + 1 
            
    if SP == EP : boat += 1
            
    # if over : boat += 1 # 50 70 80
    # else :              # 30 40 50 60 70 80
    #     if SP == EP : boat += 1
        
    return boat        


# def solution(people, limit):
#     people.sort()
#     S, E = 0 , len(people)-1    
#     boat = rest = 0
#     over = 0
#     while S != E and S < E:
#         if people[S] + people[E] <= limit:
#             boat += 1
#             S, E = S + 1, E - 1
#             over = 0
#         else: 
#             E -= 1
#             rest += 1
#             over = 1
#     if over : boat += 1
#     if not over and S==E : boat += 1        
#     boat += rest
#     return boat    
     

