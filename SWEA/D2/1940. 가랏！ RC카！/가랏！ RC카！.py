Test = int(input())

for T in range(Test):
    move_cnt = int(input())
    
    distance = 0
    speed = 0
    for mc in range(move_cnt):
        command = list(map(int,input().split()))
        
        if command[0] == 0 : speed += 0 ; distance += speed # 정지
        elif command[0] == 1 : speed += command[1] ; distance += speed # 가속
        elif command[0] == 2: 
            if speed != 0 :
                speed -= command[1]
                distance += speed # 감속
            else : speed -= 0 ; distance += speed
                
    print(f'#{T+1} {distance}')
        