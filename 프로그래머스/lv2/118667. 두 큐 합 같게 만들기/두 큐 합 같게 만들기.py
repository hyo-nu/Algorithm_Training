from collections import deque

def solution(queue1, queue2):
    Q1 = deque(queue1)
    Q2 = deque(queue2)
    Q1_sum = sum(Q1)
    Q2_sum = sum(Q2)
        
    count = 0
    while Q1_sum != Q2_sum:
        if Q1_sum > Q2_sum:
            Q1_sum -= Q1[0]
            Q2_sum += Q1[0]
            Q2.append(Q1.popleft())
            count += 1
            
        elif Q1_sum < Q2_sum:
            Q2_sum -= Q2[0]
            Q1_sum += Q2[0]
            Q1.append(Q2.popleft())
            count += 1
            
        if not Q1 or not Q2 or count >=239000:
            count = -1
            break
    
    return count

