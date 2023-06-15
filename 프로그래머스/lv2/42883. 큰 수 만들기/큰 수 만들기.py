def solution(number, k):
    answer = ''
    remove = 0
    for i in range(len(number)):
        while k > remove and answer and answer[-1] < number[i] :
            answer = answer[:-1]
            remove += 1
        answer += number[i]
    return answer[:len(answer)-(k-remove)]

