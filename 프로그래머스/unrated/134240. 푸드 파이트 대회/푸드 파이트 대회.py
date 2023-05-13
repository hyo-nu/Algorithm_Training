# 왼쪽에서 오른쪽
# 오른쪽에서 왼쪽
# 칼로리 낮은거 부터
def solution(food):
    foods_forward = ''
    foods_reverse = ''
    
    for cal in range(1,len(food)):
        foods_forward = foods_forward + str(cal) * (food[cal] // 2)
        foods_reverse = str(cal) * (food[cal] // 2) + foods_reverse
    
    return foods_forward + '0' + foods_reverse
