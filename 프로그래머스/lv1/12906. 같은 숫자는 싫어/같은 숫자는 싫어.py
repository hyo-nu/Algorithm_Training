from collections import deque
def solution(arr):
    Q = deque()    
    Q.appendleft(arr.pop())
    while arr:
        right = arr.pop()
        if right != Q[0]:
            Q.appendleft(right)
    Q = list(Q)
    return Q