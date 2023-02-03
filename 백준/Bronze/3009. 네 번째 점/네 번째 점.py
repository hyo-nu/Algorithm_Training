x_lst = []
y_lst = []

for a in range(3):
    x,y = map(int,input().split())
    x_lst.append(x)
    y_lst.append(y)

x_lst.sort()
y_lst.sort()
xy_lst = []
xy_lst.append(x_lst)
xy_lst.append(y_lst)

for b in xy_lst:
    count = 0
    for c in range(1,len(b)):
        if b[0] == b[c]:
            count += 1
    if count == 1: # 마지막 값 출력
        print(b[2], end=' ')
    elif count == 0: # 첫번쨰 값 출력
        print(b[0], end=' ')
