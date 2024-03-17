def solution(tickets):
    spot_dict = {}
    for sp, ep in tickets:
        spot_dict[sp] = spot_dict.get(sp, []) + [ep]
    
    for key in spot_dict.keys():
        spot_dict[key].sort(reverse = True)

    for k,v in spot_dict.items():print(k,v)
    
    stack = ["ICN"]
    route = []    
    
    while stack:
        sp = stack[-1]
        
        if sp in spot_dict and spot_dict[sp]:
            stack.append(spot_dict[sp].pop())
        else : 
            route.append(stack.pop())
            
    return route[::-1]


# def solution(tickets):
#     routes = {}
#     for t in tickets:
#         routes[t[0]] = routes.get(t[0], []) + [t[1]]
    
#     for r in routes:
#         routes[r].sort(reverse=True)
    
#     stack = ['ICN']
#     path = []
    
#     while stack:
#         top = stack[-1]
        
#         if top in routes and routes[top]:
#             stack.append(routes[top].pop())
        
#         else:
#             path.append(stack.pop())
#         print("stack : ",stack)
#         print("path : ",path)
        
            
#     return path[::-1]