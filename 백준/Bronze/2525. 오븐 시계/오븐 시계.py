h, m = map(int,input().split())
time = int(input())

if m + time >= 60:
    h = h + (m + time) // 60
    m = (m + time) % 60
    if h >= 24:
        h = h-24
else:
    m = m+time
    
print(h,m)