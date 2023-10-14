def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    Sum = 0
    for i in range(len(A)):
        Sum += A[i] * B[i]
        
    return Sum