while True:
    lst = list(map(int,input().split()))
    lst.sort()
    if 0 in lst:break
    if lst[2]**2 == lst[1]**2 + lst[0]**2:print('right')
    else:print('wrong')