def point(dire,dist):
    if dire == 1 : return [0, dist]
    elif dire == 2 : return [row, dist]
    elif dire == 3 : return [dist, 0]
    elif dire == 4 : return [dist, col]

def Min(lst):
    if nr == 0 and lst[0] == row :
        result = row + (nc + lst[1])
        if result >= (row + col): result = ((row + col)*2) - result
    elif nr == row and lst[0] == 0 :
        result = row + (nc + lst[1])
        if result >= (row + col): result = ((row + col)*2) - result
    elif nc == 0 and lst[1] == col :
        result = col + (nr + lst[0])
        if result >= (row + col): result = ((row + col)*2) - result
    elif nc == col and lst[1] == 0 :
        result = col + (nr + lst[0])
        if result >= (row + col): result = ((row + col)*2) - result
        
    else:result = abs(lst[0]-nr) + abs(lst[1]-nc)

    return result

# N 가로 , M 세로
# col   , row
col,row = map(int,input().split())
shop = int(input())
G = [[0]*(col+1) for _ in range(row+1)]
shop_lst = []

# 상점 방향 1:북,2:남,3:서,4:동
# 북남 : 왼쪽에서의거리 , 동서 : 위쪽에서의거리
for i in range(shop):
    dire,dist = map(int,input().split())
    shop_lst.append(point(dire, dist))

result = 0
r, c = map(int,input().split())
nr,nc = point(r,c)

for lst in shop_lst:
    result += Min(lst)
print(result)