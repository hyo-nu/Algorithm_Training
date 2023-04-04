def back(N,cnt):
    global Min
    if Min <= cnt : return
    if N == 1:
        Min = min(Min,cnt)
        return
    if N % 3 == 0 : back(N/3,cnt+1)
    if N % 2 == 0 : back(N/2,cnt+1)
    back(N-1,cnt+1)

N = int(input())
Min = 10 ** 6 + 1
back(N,0)
print(Min)