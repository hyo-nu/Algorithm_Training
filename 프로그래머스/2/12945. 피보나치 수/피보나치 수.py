def solution(n):
    if n == 1 : return 1
    elif n == 0 : return 0
    
    return (solution(n-1) + solution(n-2)) % (1234567)