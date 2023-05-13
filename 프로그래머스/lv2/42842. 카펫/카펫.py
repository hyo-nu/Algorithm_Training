# 8 <= 갈색 <= 5,000
# 1 <= 노랑 <= 2,000,000
# 가로 >= 세로

# def solution(brown, yellow):    
#     for L in range(1, yellow // 2 + 1):
        
#         if yellow % L == 0: 
#             W = yellow // L 
#         else : continue
        
#         if (W * 2) + (L * 2) + 4 == brown: 
#             return [W + 2,L + 2]
        
def solution(brown, yellow):
    
    for i in range(1,yellow//2+2):
        if yellow % i == 0:
            length = i# 세로
            width = yellow // i # 가로
            
        if (length*2)+(width*2)+4 == brown:
            return [width+2,length+2]
    
