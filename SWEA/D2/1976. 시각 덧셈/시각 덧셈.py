Test = int(input())

for T in range(Test):
    time = list(map(int,input().split()))
    
    hour = 0
    minute = 0
    
    for t in range(len(time)):
        if t % 2 == 0 : hour += time[t]         
        else : minute += time[t]
    
    if minute >= 60:
        minute -= 60
        hour += 1
        while hour > 12:
            hour = hour - 12
    while hour > 12:
            hour = hour - 12  
        
    print(f'#{T+1} {hour} {minute}')
        