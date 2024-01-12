def solution(numbers):
    result = []
    for num in numbers:
        x = list("0" + format(num,'b'))
        
        for i in range(len(x)-1, -1, -1):
            if i != len(x) - 1 and x[i] == "0":
                x[i], x[i+1] = "1", "0"
                break
                
            elif i == len(x) - 1 and x[i] == "0":
                x[i] = "1"
                break
                
        result.append(int("".join(x),2))
    
    return result

# def solution(numbers):
#     answer = []
#     for i in range(1, 25):
#             print(i," : ", format(i,'b').zfill(5))
    
#     for num in [3,7,9,11,13,15]:
#         x = format(num,'b')
#         plus = 0
        
#         while True:
#             diff = 0
#             plus += 1
#             y = format(num + plus,'b')
#             for i in range(-1,-(len(x))-1,-1):
#                 if x[i] != y[i] : diff += 1
#                 if diff > 2 : break
#             else:
#                 x_len = len(x)
#                 dx = (len(y) - x_len) * "0"
#                 for i in range(len(y) - x_len):
#                     if dx[i] != y[i] : diff += 1
#                     if diff > 2 : break
                
#             if diff <= 2 : 
#                 print(num, "일 때", num + plus )
#                 answer.append(num + plus) ; break
                
#     return answer

