spot_n = int(input())
spot_point_lst = [0]*5


for n in range(spot_n):
    x,y = map(int,input().split())
    
    if x > 0 and y > 0: # 제1사분면
        spot_point_lst[0] += 1 
    elif x < 0 and y > 0: # 제2사분면
        spot_point_lst[1] += 1
    elif x < 0 and y < 0: # 제3사분면
        spot_point_lst[2] += 1
    elif x > 0 and y < 0: # 제4사분면
        spot_point_lst[3] += 1
    elif x == 0 or y == 0: # 축위
        spot_point_lst[4] += 1

for c in range(len(spot_point_lst)):
    if c != len(spot_point_lst)-1:
        print(f'Q{c+1}: {spot_point_lst[c]}')
    elif c == len(spot_point_lst)-1:
        print(f'AXIS: {spot_point_lst[c]}')