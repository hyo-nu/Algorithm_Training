def solution(numbers, hand):
    
    left = [1,4,7]
    right = [3,6,9]
    hand_L = -1
    hand_R = -2
    hands = ''
    key = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
    
    for i in range(len(numbers)):
        if numbers[i] in left : 
            hands += 'L'
            hand_L = numbers[i]
        elif numbers[i] in right : 
            hands += 'R' 
            hand_R = numbers[i]
        else:
            for r in range(4):
                for c in range(3):
                    if key[r][c] == numbers[i] : tx,ty = r,c
                    if key[r][c] == hand_R : rx,ry = r,c
                    elif key[r][c] == hand_L : lx,ly = r,c
            R_d = abs(tx-rx) + abs(ty-ry)
            L_d = abs(tx-lx) + abs(ty-ly)
            if R_d > L_d:
                hands += 'L'
                hand_L = numbers[i]
            elif R_d < L_d:
                hands += 'R'
                hand_R = numbers[i]
            else:
                if hand == 'right':
                    hands += 'R'
                    hand_R = numbers[i]
                else:
                    hands += 'L'
                    hand_L = numbers[i]
    return hands