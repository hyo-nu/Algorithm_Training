h, m, s = map(int,input().split())
D = int(input())

if s + D >= 60: # 60초 넘어간 경우
    m = m + (s+D) // 60 
    s = (s+D) % 60 

    if m >= 60: # 넘긴 분을 더했을 때 60분 넘긴 경우
        h = h + m // 60
        m = m % 60
  
        if h >= 24: # 24시가 넘어간 경우
            h = h % 24
else:
    s = s+D

print(h,m,s)