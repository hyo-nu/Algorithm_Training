# def solution(number, k):
#     answer = ''
#     remove = 0
#     for i in range(len(number)):
#         while k > remove and answer and answer[-1] < number[i] :
#             answer = answer[:-1]
#             remove += 1
#         answer += number[i]
#     return answer

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])